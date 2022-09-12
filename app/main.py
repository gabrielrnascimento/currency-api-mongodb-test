from fastapi import FastAPI, HTTPException

from app.model import Currency
from app.database import (
    get_all_quotes,
    get_one_quote,
    create_quote,
    update_quote,
    delete_quote
)



app = FastAPI()

@app.get("/")
def root():
    return "Hello World!"

@app.get("/quotes")
def get_all_coins():
    res = get_all_quotes()
    return res

@app.get("/quote/{currency_code}")
def get_coin(currency_code: str):
    return get_one_quote(currency_code)

@app.post("/quote/")
def create_coin(currency_data: Currency):
    quote = create_quote(currency_data)
    return quote

@app.put("/quote/{currency_code}")
def update_coin(currency_code: str, currency_data: Currency):
    updated = update_quote(currency_code, currency_data)
    return 

@app.delete("/quote/{currency_code}")
def delete_coin(currency_code: str):
    return delete_quote(currency_code)