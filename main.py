import time
from binance.client import Client
from playsound import playsound

api_key = # Paste here your api_key
secret_key = # Paste here your secret key

symb = "BTCUSDT" # Set here the symbol
max_price = 0 # Set here the max price
min_price = 0 # Set here the min price

client = Client(api_key, secret_key)
counter = 0
while counter <= 100:
    depth = client.get_recent_trades(symbol=symb)
    ethusdt = depth[0]
    currprice = float(ethusdt["price"])
    print (ethusdt["price"])
    if currprice > max_price:
        playsound("alarm.mp3")
    elif currprice < min_price:
        playsound("alarm.mp3")
    else:
        time.sleep(1)
        counter += 1

