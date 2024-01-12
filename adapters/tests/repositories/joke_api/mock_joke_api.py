from core.src.repository import JokeRepository
import requests, json
from core.src.models import Joke
from factories.config import MockJokeAPIConfig
from core.src.exceptions import JokeRepositoryException

class MockJokeAPIRepository(JokeRepository):
    def get_joke(self) -> Joke:
        try:  
            api_url = MockJokeAPIConfig.MOCK_JOKE_API_URL
            response = requests.get(api_url)
            if response.status_code == requests.codes.ok:
               return Joke(joke_value=json.loads(response.text)[0].get("joke"))
            else:
                return ("Error:", response.status_code, response.text)
        except Exception as e:
            raise JokeRepositoryException(method="get_joke")