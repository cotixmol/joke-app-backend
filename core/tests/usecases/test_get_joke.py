from dotenv import load_dotenv
load_dotenv()
from typing import Callable
from pydantic import ValidationError
import pytest
from requests.exceptions import HTTPError
from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository
from adapters.tests.repositories import MockJokeAPIRepository
from core.src.exceptions import JokeRepositoryException, JokeBusinessException
from core.src.usecases import GetJoke
from core.src.models import Joke

class TestGetJokeMemoryRepository():
    def test__get_joke__return_jokes__when_there_are_jokes_in_repository(self, joke_factory: Callable) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()
        joke = joke_factory()
        joke_repository.add_joke(joke)

        get_joke = GetJoke(joke_repository)
        joke_response = get_joke()

        expected_joke_response = joke
        assert joke_response == expected_joke_response
    
    def test__get_joke__returns_none__when_there_are_no_jokes_in_repository(self) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()

        get_joke = GetJoke(joke_repository)
        joke_response = get_joke()

        assert joke_response == None
    
    def test__get_joke__raises_business_exception__when_repository_is_incorrect(self) -> None:
        joke_repository: JokeRepository = None

        get_joke = GetJoke(joke_repository)

        with pytest.raises(JokeBusinessException):
            get_joke()
        
    def test__add_joke__add_a_valid_joke_to_the_memory_instance__when_add_joke_method_is_used(self):
        joke_repository: JokeRepository = MemoryJokeRepository()

        joke = Joke(joke_value="This is a joke")
        joke_repository.add_joke(joke)

        assert len(joke_repository.jokes) == 1
        assert joke_repository.jokes[0].joke_value == "This is a joke"

class TestJokeTyping():
    def test__pydantic_joke_model__raises_validation_exception__when_the_joke_value_is_a_non_string_value(self):
        joke_repository: JokeRepository = MemoryJokeRepository()

        with pytest.raises(ValidationError) as e:
            invalid_joke = Joke(joke_value=123)
            joke_repository.add_joke(invalid_joke)
        assert "Input should be a valid string" in str(e.value)

    def test__add_joke__raises_joke_repository_exception__when_the_joke_value_is_a_non_string_value(self):
        joke_repository: JokeRepository = MemoryJokeRepository()
        invalid_joke = Joke(joke_value="Valid String")
        invalid_joke.joke_value = 123

        with pytest.raises(JokeRepositoryException) as e:
            joke_repository.add_joke(invalid_joke)
        assert "Something was wrong trying to add_joke the Joke" in str(e.value)

class TestGetJokeMethod():
    def test__returns_a_joke__when_api_is_available(self, mocker):
        joke_repository: JokeRepository = mocker.Mock(spec=JokeRepository)
        joke_repository.get_joke = mocker.Mock(return_value="Some Joke")

        get_joke = GetJoke(joke_repository) #Due to the __call__ it is a function
        joke = get_joke()

        assert joke == "Some Joke"

    def test__mocked_get_joke__returns_none_value__when_mock_repository_response_is_passed_as_none(self, mocker):
        joke_repository: JokeRepository = mocker.Mock(spec=JokeRepository)
        joke_repository.get_joke = mocker.Mock(return_value=None)

        get_joke = GetJoke(joke_repository)
        joke = get_joke()

        assert joke is None

    def test__mocked_get_joke__business_exception__when_mock_repository_exception_side_effect_is_passed(self, mocker):
        joke_repository: JokeRepository = mocker.Mock(spec=JokeRepository)
        joke_repository.get_joke = mocker.Mock(side_effect=Exception("Everything is wrong"))

        get_joke = GetJoke(joke_repository)

        with pytest.raises(JokeBusinessException):
            get_joke()
        
class TestGetJokeMockAPIRepository():
    def test__get_joke__return_a_valid_answer__when_we_call_api_repository(self):
        joke_repository: JokeRepository = MockJokeAPIRepository()

        get_joke = GetJoke(joke_repository)
        joke_response = get_joke()

        assert joke_response is not None
        assert isinstance(joke_response, Joke)

    def test__get_joke__returns_joke_repository_exception__when_api_response_is_an_error(self, mocker):
        mocker.patch('requests.get', side_effect=HTTPError("API error"))

        joke_repository = MockJokeAPIRepository()
        
        with pytest.raises(JokeRepositoryException):
            joke_repository.get_joke()