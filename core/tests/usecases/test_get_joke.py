from dotenv import load_dotenv
load_dotenv()
from typing import Callable
import pytest
from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository
from core.src.exceptions import JokeRepositoryException, JokeBusinessException
from core.src.usecases import GetJoke
from core.src.models import Joke


class TestGetJoke:
    def test_get_joke_when_there_is_jokes(self, joke_factory: Callable) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()
        joke = joke_factory()
        joke_repository.add_joke(joke)
        get_joke_use_case = GetJoke(joke_repository)
        joke_response = get_joke_use_case.execute()
        expected_joke_response = joke
        assert joke_response == expected_joke_response
    
    def test_get_joke_retrieves_none_when_there_is_no_jokes(self) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()
        get_joke_use_case = GetJoke(joke_repository)
        joke_response = get_joke_use_case.execute()
        assert joke_response == None
    
    def test_should_raise_business_exception_when_repository_is_incorrect(self) -> None:
        joke_repository: JokeRepository = None
        get_joke_use_case = GetJoke(joke_repository)
        with pytest.raises(JokeBusinessException):
            get_joke_use_case.execute()

class TestMemoryJokeRepository:
    def test_add_joke_raises_exception_for_non_string_joke_value(self):
        joke_repository = MemoryJokeRepository()
        invalid_joke = Joke(joke_value=123)
        with pytest.raises(JokeRepositoryException) as e:
            joke_repository.add_joke(invalid_joke)
        assert "Something was wrong trying to add_joke the Joke" in str(e.value)