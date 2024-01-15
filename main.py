from fastapi import FastAPI
from api.routers import joke
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

app.include_router(joke, prefix="/jokes")
