from core.src.repository import JokeRepository
import requests
import json
from core.src.models import Joke
from factories.config import MockJokeAPIConfig
from core.src.exceptions import JokeRepositoryException


class MockJokeAPIRepository(JokeRepository):
    def get_joke(self) -> Joke:
        try:
            api_url = MockJokeAPIConfig.MOCK_JOKE_API_URL
            response = requests.get(api_url)
            return Joke(joke_value=json.loads(response.text)[0].get("joke"))
        except Exception:
            raise JokeRepositoryException(method="get_joke")
