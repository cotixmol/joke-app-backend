import json
import requests
from core.src.repository import JokeRepository
from core.src.models import Joke
from factories.config import JokeAPIConfig
from core.src.exceptions import JokeRepositoryException


class JokeAPIRepository(JokeRepository):
    def get_joke(self) -> Joke:
        try:
            limit = JokeAPIConfig.LIMIT
            api_url = JokeAPIConfig.JOKE_API_URL.format(limit)
            response = requests.get(api_url, headers={'X-Api-Key': JokeAPIConfig.JOKE_API_KEY})
            if response.status_code == requests.codes.ok:
                return Joke(joke_value=json.loads(response.text)[0].get("joke"))
            else:
                return ("Error:", response.status_code, response.text)
        except Exception:
            return JokeRepositoryException(method="get_joke")
