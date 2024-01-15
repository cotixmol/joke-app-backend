from fastapi import APIRouter, Depends, status
from core.src.models import Joke
from core.src.usecases import GetJoke
from adapters.src.repositories import JokeAPIRepository
from fastapi.responses import JSONResponse


joke = APIRouter()


def get_joke_from_api_use_case() -> GetJoke:
    return GetJoke(JokeAPIRepository())


@joke.get("/")
async def get_joke_handler(get_joke: GetJoke = Depends(get_joke_from_api_use_case)) -> Joke:
    try:
        joke_response = get_joke()
        return JSONResponse(content=joke_response, status_code=status.HTTP_200_OK)
    except Exception as e:
        return JSONResponse(content=str(e), status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
