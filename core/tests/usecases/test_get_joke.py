from core.src.repository import JokeRepository
from adapters.src.repositories import MemoryJokeRepository

def test_get_joke():
    joke_repository: JokeRepository = MemoryJokeRepository()
    pass
