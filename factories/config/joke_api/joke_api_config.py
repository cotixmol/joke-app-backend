from ..utils import parse_env_variable


class JokeAPIConfig:
    JOKE_API_URL: str = parse_env_variable("JOKE_API_URL")
    JOKE_API_KEY: str = parse_env_variable("JOKE_API_KEY")
    LIMIT: str = parse_env_variable("LIMIT")
