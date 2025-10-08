from typing import Annotated
from fastapi import Header


class JWTTokenValidation:
    def __init__(self):
        self.headers = None

    def __call__(self, authorization: Annotated[str, Header()]):
        print(authorization)
        return self


JWTValidation = JWTTokenValidation()
