from binance.client import Client
from dotenv import load_dotenv 
import os
import time
import pandas as pd

# gets API keys from .env
load_dotenv()


client = Client(os.getenv("BINANCE_API_KEY"), os.getenv("BINANCE_SECRET"))

  


# prints price of BTC/USDT every 5 seconds
#while True:
#    price = client.get_symbol_ticker(symbol="BTCUSDT")
#    print(f"BTC: ${float(price['price']):,.2f}")
#    time.sleep(5)  # fetch every 5 seconds