import time
from binance.client import Client
from playsound import playsound

api_key = ""# Paste here your api_key
secret_key = ""# Paste here your secret key

symb = "BTCUSDT" # Set here the symbol
max_price = 0 # Set here the max price
min_price = 0 # Set here the min price

client = Client(api_key, secret_key)
depth = client.get_recent_trades(symbol=symb)
ethusdt = depth[0]
currprice = float(ethusdt["price"])
while currprice > max_price and currprice < min_price:
    depth = client.get_recent_trades(symbol=symb)
    ethusdt = depth[0]
    currprice = float(ethusdt["price"])
    print (ethusdt["price"])
    time.sleep(1)
playsound("alarm.mp3")
