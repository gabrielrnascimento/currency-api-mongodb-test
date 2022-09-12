import pymongo
from datetime import datetime

from app.model import Currency



client = pymongo.MongoClient("mongodb://root:password@mongodb")
db = client.challenge_bravo
quotes = db.quotes


def get_all_quotes():
    quote_list = list(quotes.find({}))
    return quote_list

def get_one_quote(currency_code: str):
    quote = quotes.find_one({"currency_code": currency_code})
    currency = Currency(**quote)
    return currency

def create_quote(currency: Currency):
    currency.currency_type = "fantasy"
    new_quote = quotes.insert_one(currency.dict())
    return currency

def update_quote(currency_code: str, currency: Currency):
    original_quote = get_one_quote(currency_code)

    currency.currency_type = original_quote.currency_type
    currency.created_at = original_quote.created_at
    currency.updated_at = datetime.utcnow()

    quotes.update_one(
        {"currency_code": currency_code},
        {"$set": currency.dict()}
    )
    updated_quote = quotes.find_one({"currency_code": currency.currency_code})
    return updated_quote

def delete_quote(currency_code: str):
    quotes.delete_one({"currency_code": currency_code})
    return





# users.insert_many(user_list)

# print(list(db.users.find()))

# print(db.users.find_one({"first_name":"Rodrigo"}))

# print(client.list_database_names())

# client.drop_database('challenge_bravo')

# print(client.list_database_names())