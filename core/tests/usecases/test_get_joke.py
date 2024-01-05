from typing import Callable
from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository
from core.src.usecases import GetJoke

class TestGetJoke:
    def test_get_joke(self, joke_factory: Callable) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository() 
        for _ in range(3):
            joke = joke_factory()
            joke_repository.add_joke(joke)
        get_joke_use_case = GetJoke(joke_repository)