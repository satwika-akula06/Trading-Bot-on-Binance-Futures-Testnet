import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()

USE_MOCK = os.getenv("USE_MOCK", "True") == "True"

def get_client():
    if USE_MOCK:
        return None  # no real client
    return Client(
        os.getenv("API_KEY"),
        os.getenv("API_SECRET"),
        testnet=True
    )