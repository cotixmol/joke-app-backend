from fastapi import APIRouter, Depends
from core.src.models import Joke
from core.src.usecases import GetJoke
from adapters.src.repositories import JokeAPIRepository

joke = APIRouter()

def get_joke_from_api_use_case() -> GetJoke:
    return GetJoke(JokeAPIRepository())

@joke.get("/")
async def get_joke(use_case: GetJoke= Depends(get_joke_from_api_use_case)) -> Joke:
    joke_response = use_case.execute() 
    return joke_response