import schedule
import time
from util import get_symbols_x_time_frames, log
from db import read

### Lists of tuple(symbol: str, timeframe: str) ###
actualization_needed = get_symbols_x_time_frames()
history_needed = [] 
###

def get_new_prices():
    log(actualization_needed)
    for symbol, time_frame in actualization_needed:
        log(symbol, time_frame)
    
    log("getting new prices for existing symbols")
    log(read(None, None))

def get_histories():
    log("getting histories for new symbols")

schedule.every(1).seconds.do(get_new_prices)
schedule.every(10).minutes.do(get_histories)

while True:
    schedule.run_pending()
    time.sleep(0.1)
