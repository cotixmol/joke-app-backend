from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from api.routers import joke

app = FastAPI()

app.include_router(joke, prefix="/jokes")