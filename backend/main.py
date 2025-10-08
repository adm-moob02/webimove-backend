from fastapi import FastAPI, Request, status, Depends
from api.core.dependencies.authjwt import JWTValidation


app = FastAPI()


@app.get("/", dependencies=[Depends(JWTValidation)])
async def hello_word(request: Request):
    return {
        "content": "Hello World"
    }
