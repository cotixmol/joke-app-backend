class RepositoryException(Exception):
    def __init__(self, entity_type: str, method: str):
        message = f"Something was wrong trying to {method} the {entity_type}"
        super().__init__(message)


class JokeRepositoryException(RepositoryException):
    def __init__(self, method: str):
        super().__init__(entity_type="Joke", method=method)
