from core.src.repository import JokeRepository
from core.src.models import Joke


class GetJoke:
    def __init__(self, joke_repository: JokeRepository):
        self.joke_repository = joke_repository

    def execute(self) -> Joke:
        try:
            joke = self.joke_repository.get_joke()
            return joke
        except Exception as e:
            raise Exception(str(e))
