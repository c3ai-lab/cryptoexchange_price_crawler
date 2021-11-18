from datetime import datetime
from time import sleep
from util import get_start_date, get_symbols_x_time_frames, get_timedelta_for_time_frame, flatten, log, to_df
from db import write
import ccxt


binance = ccxt.binance()

START_DATE = get_start_date()

def get_full_history(symbol, time_frame):
    start_mts = int(START_DATE.timestamp() * 1000)
    timedelta_ms = get_timedelta_for_time_frame(time_frame).total_seconds() * 1000
    
    current_mts = start_mts
    last_mts = int(datetime.now().timestamp() * 1000)

    data = []

    while current_mts < last_mts:
        new_data = binance.fetch_ohlcv(symbol, timeframe=time_frame, since=current_mts)
        data.append(new_data)

        current_mts += timedelta_ms * len(new_data)
        current_mts = int(current_mts)

        sleep(0.334)

    return to_df(flatten(data), symbol, time_frame)

if __name__ == '__main__':
    for symbol, time_frame in get_symbols_x_time_frames():
        write(get_full_history(symbol, time_frame))