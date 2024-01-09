from dotenv import load_dotenv
load_dotenv()
from typing import Callable
from pydantic import ValidationError
import pytest
import unittest
from unittest.mock import MagicMock
from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository
from core.src.exceptions import JokeRepositoryException, JokeBusinessException
from core.src.usecases import GetJoke
from core.src.models import Joke

#Sociable Unit Testing
class TestGetJoke():
    def test__get_joke__return_jokes__when_there_are_jokes_in_repository(self, joke_factory: Callable) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()
        joke = joke_factory()
        joke_repository.add_joke(joke)

        get_joke_use_case = GetJoke(joke_repository)
        joke_response = get_joke_use_case.execute()

        expected_joke_response = joke
        assert joke_response == expected_joke_response
    
    def test__get_joke__returns_none__when_there_are_no_jokes_in_repository(self) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()

        get_joke_use_case = GetJoke(joke_repository)
        joke_response = get_joke_use_case.execute()

        assert joke_response == None
    
    def test__get_joke__raises_business_exception__when_repository_is_incorrect(self) -> None:
        joke_repository: JokeRepository = None

        get_joke_use_case = GetJoke(joke_repository)

        with pytest.raises(JokeBusinessException):
            get_joke_use_case.execute()
        
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

#Solitary Unit Testing
class TestGetJokeMockRepository(unittest.TestCase):
    def test__mocked_get_joke__returns_mock_value__when_mock_repository_response_is_passed_as_valid_joke(self):
        joke_repository: JokeRepository = MagicMock()
        joke_repository.get_joke.return_value = "Coti's Joke"

        get_joke_use_case = GetJoke(joke_repository)
        joke = get_joke_use_case.execute()

        self.assertEqual(joke, "Coti's Joke")

    def test__mocked_get_joke__returns_none_value__when_mock_repository_response_is_passed_as_none(self):
        joke_repository: JokeRepository = MagicMock()
        joke_repository.get_joke.return_value = None

        get_joke_use_case = GetJoke(joke_repository)

        joke = get_joke_use_case.execute()
        self.assertIsNone(joke)

    def test__mocked_get_joke__business_exception__when_mock_repository_exception_side_effect_is_passed(self):
        mock_repository: JokeRepository = MagicMock()
        mock_repository.get_joke.side_effect = Exception("Everything is wrong")

        get_joke_use_case = GetJoke(mock_repository)

        with self.assertRaises(JokeBusinessException):
            get_joke_use_case.execute()
