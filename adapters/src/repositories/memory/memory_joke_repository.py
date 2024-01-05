from core.src.repository import JokeRepository
from core.src.models import Joke

FIRST_ITEM = 0


class MemoryJokeRepository(JokeRepository):
    def __init__(self):
        self.jokes = []

    def get_joke(self):
        if self.jokes:
            return self.jokes[FIRST_ITEM]
        else:
            return None

    def add_joke(self, joke: Joke):
        self.jokes.append(joke)
