from . import joke
from core.src.exceptions import JokeBusinessException
from fastapi import status
from fastapi.responses import JSONResponse
import pytest


class TestGetJokeRouter():
    @pytest.mark.asyncio
    async def test__returns_a_200__when_router_is_called(self, faker, mocker):
        fake_joke = faker.sentence()
        get_joke = mocker.Mock(return_value=fake_joke)
        expected_response = JSONResponse(content=fake_joke, status_code=status.HTTP_200_OK)

        response = await joke.get_joke_handler(get_joke)

        assert get_joke.called
        assert response.body == expected_response.body
        assert response.status_code == expected_response.status_code

    @pytest.mark.asyncio
    async def test__returns_a_500__when_router_is_called(self, mocker):
        error_text = "Internal Server Error"
        get_joke = mocker.Mock(side_effect=Exception(error_text))
        expected_response = JSONResponse(content=error_text, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

        response = await joke.get_joke_handler(get_joke)

        assert get_joke.called
        assert response.body == expected_response.body
        assert response.status_code == expected_response.status_code

    @pytest.mark.asyncio
    async def test__returns_a_business_exception__when_router_is_called(self, mocker):
        get_joke = mocker.Mock(
            side_effect=JokeBusinessException("Business Exception")
        )
        expected_response = JSONResponse(
            content="Business Exception", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

        response = await joke.get_joke_handler(get_joke)

        assert get_joke.called
        assert response.body == expected_response.body
        assert response.status_code == expected_response.status_code
