import random
from core.src.repository import JokeRepository
from core.src.models import Joke

class MemoryJokeRepository(JokeRepository):
    def __init__(self):
        self.jokes = [] 

    def get_joke(self):
        if self.jokes:
            return random.choice(self.jokes)
        else:
            return None 
    
    def add_joke(self, joke: Joke):
        self.jokes.append(joke)

