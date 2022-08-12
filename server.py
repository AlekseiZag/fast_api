from typing import Union
from starlette.responses import Response
from fastapi import FastAPI, Body, Form, Cookie

from services import unify_phone

app = FastAPI()


@app.post("/unify_phone_from_json")
def index_page(body=Body(...)):
    """Преобразование телефона к стандартизированному виду из JSON"""
    result = unify_phone(phone=body.get('phone'))
    return Response(result, media_type='text/html')


@app.post("/unify_phone_from_form")
def index_page(phone: str = Form(...)):
    """Преобразование телефона к стандартизированному виду из формы"""
    result = unify_phone(phone=phone)
    return Response(result, media_type='text/html')


@app.get("/unify_phone_from_query")
def index_page(phone: str):
    """Преобразование телефона к стандартизированному виду из query params"""
    result = unify_phone(phone=phone)
    return Response(result, media_type='text/html')


@app.post("/unify_phone_from_cookies")
def index_page(phone: Union[str, None] = Cookie(default=None)):
    """Преобразование телефона к стандартизированному виду из query params"""
    result = unify_phone(phone=phone)
    return Response(result, media_type='text/html')
