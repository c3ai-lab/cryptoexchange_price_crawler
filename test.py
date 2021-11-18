import ccxt
from datetime import datetime, timedelta

# # print(ccxt.exchanges)
# binance = ccxt.binance()
# binance_markets = binance.load_markets()

# btc_data = binance.fetch_ohlcv('BTCUSDT', since=int(datetime(2020,1,1).timestamp() * 1000))

# print(len(btc_data))

# import yaml

# with open("config.yml", "r") as stream:
#     try:
#         print(yaml.safe_load(stream))
#     except yaml.YAMLError as exc:
#         print(exc)
# from itertools import cycle

# symbols = [1,2,3]
# time_frames = ['a', 'b', 'c']

# def flatten(t):
#     return [item for sublist in t for item in sublist]

# print(flatten([list(zip(cycle([symbol]), time_frames)) for symbol in symbols]))

from src.util import get_time_frame

print(timedelta(**get_time_frame('1W')['timedelta']))