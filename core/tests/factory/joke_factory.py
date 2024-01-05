from typing import Any, Callable
from faker import Faker
from pytest import fixture
from core.src.models import Joke


@fixture
def joke_factory() -> Callable:
    faker = Faker()

    def _factory(**kwargs: Any) -> Joke:
        return Joke(
            **{
                **{
                    "joke_value": faker.sentence(),
                },
                **kwargs,
            }
        )

    return _factory
