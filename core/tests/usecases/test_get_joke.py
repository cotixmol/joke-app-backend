from typing import Callable
from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository

class TestGetJoke:
    def test_get_joke(self, joke_factory: callable) -> None:
        joke_repository: JokeRepository = MemoryJokeRepository()
        joke = joke_factory()
        pass
