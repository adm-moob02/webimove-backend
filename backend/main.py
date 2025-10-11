from api.core.dependencies.authjwt import JWTValidation
from fastapi import Depends
from fastapi import FastAPI
from fastapi import Request


app = FastAPI()


@app.get("/", dependencies=[Depends(JWTValidation)])
async def hello_word(request: Request):
    return {
        "content": "Hello World"
    }
