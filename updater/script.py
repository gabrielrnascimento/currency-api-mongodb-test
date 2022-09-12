from datetime import datetime
from time import sleep
import pymongo
import requests

from model import Currency



client = pymongo.MongoClient("mongodb://root:password@mongodb")

db = client.challenge_bravo
quotes = db.quotes

def get_latest_quotes():
    res = requests.get('https://api.coinbase.com/v2/exchange-rates', params={'currency': 'USD'})
    return res.json()['data']['rates']

currencies = get_latest_quotes()
currency_list = []

print(f"updating at {datetime.utcnow()}")
for currency_code, rate in currencies.items():
    currency = Currency(currency_code=currency_code, rate=rate, currency_type="oficial")
    quotes.find_one_and_update(
        filter={"currency_code": currency.currency_code}, 
        update={"$set": currency.dict()}, 
        upsert=True)


while True:
    sleep(600)
    print(f"updating at {datetime.utcnow()}")
    updated_currencies = get_latest_quotes()
    for currency_code, rate in updated_currencies.items():
        currency = Currency(currency_code=currency_code, rate=rate)
        quotes.update_one(
            filter={"currency_code": currency.currency_code}, 
            update={"$set": {
                "rate": currency.rate,
                "updated_at": datetime.utcnow()
                }}
            )