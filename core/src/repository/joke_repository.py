from abc import ABC, abstractmethod

class JokeRepository(ABC):
    @abstractmethod
    def get_joke(self):
        raise NotImplementedError