from pydantic import BaseModel

class Joke(BaseModel):
    joke_value: str
