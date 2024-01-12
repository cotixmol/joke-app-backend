from core.src.repository import JokeRepository
from core.src.models import Joke
from core.src.exceptions import JokeBusinessException


class GetJoke:
    def __init__(self, joke_repository: JokeRepository):
        self.joke_repository = joke_repository

    def __call__(self) -> Joke:
        try:
            joke = self.joke_repository.get_joke()
            return joke
        except Exception:
            raise JokeBusinessException()
