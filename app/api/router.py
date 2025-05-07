from fastapi import FastAPI
from fastapi.responses import JSONResponse
from api.schemas import Message
from html import HTTPStatus

app = FastAPI()


@app.get('/', status_code=HTTPStatus.ok, response_model=Message)
def read_root():
    return JSONResponse(content={'mensage': 'Olar Mundo'})
