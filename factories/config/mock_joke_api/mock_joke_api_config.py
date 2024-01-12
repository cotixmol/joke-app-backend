from ..utils import parse_env_variable

class MockJokeAPIConfig:
    MOCK_JOKE_API_URL: str = parse_env_variable("MOCK_JOKE_API_URL")