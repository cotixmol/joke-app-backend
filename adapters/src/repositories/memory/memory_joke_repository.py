from core.src.repository import JokeRepository
from core.src.models import Joke
from core.src.exceptions import JokeRepositoryException

FIRST_ITEM = 0


class MemoryJokeRepository(JokeRepository):
    def __init__(self):
        self.jokes = []

    def get_joke(self):
        try:
            if self.jokes:
                return self.jokes[FIRST_ITEM]
            else:
                return None
        except Exception:
            raise JokeRepositoryException(method="get_joke")

    def add_joke(self, joke: Joke):
        if not isinstance(joke.joke_value, str):
            raise JokeRepositoryException(method="add_joke")
        self.jokes.append(joke)
