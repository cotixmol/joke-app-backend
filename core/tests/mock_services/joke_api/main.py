from fastapi import FastAPI
import json
import random

joke_app = FastAPI()

with open('jokes.json', 'r') as file:
    jokes = json.load(file)


@joke_app.get("/joke")
async def get_joke():
    random_joke = random.choice(jokes)
    return [random_joke]
