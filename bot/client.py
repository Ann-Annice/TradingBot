from binance.client import Client
from dotenv import load_dotenv
import os

# Load .env variables
load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Create Binance client
client = Client(API_KEY, API_SECRET)

# Binance Futures Testnet URL
client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

def get_client():
    return client