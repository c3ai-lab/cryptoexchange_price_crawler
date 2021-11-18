from typing import List
import yaml
from itertools import cycle
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
from sqlalchemy import create_engine
import pandas as pd


load_dotenv()

def log(*args, **kwargs):
    '''
    Prints if DEBUG_MODE is set to True in .env.
    '''
    if os.getenv('DEBUG_MODE') == 'True': # is a str in .env
        print(*args, **kwargs)

def get_start_date() -> datetime:
    '''
    Returns the global start date, the earliest point in time we want to retrieve data from.
    '''
    return datetime(
        int(os.getenv('DATA_FROM_YEAR')),
        int(os.getenv('DATA_FROM_MONTH')),
        int(os.getenv('DATA_FROM_DAY')),
    )

def flatten(t) -> List:
    return [item for sublist in t for item in sublist]

def get_config():
    '''
    Returns the config file as dict.
    '''
    with open("config.yml", "r") as stream:
        return yaml.safe_load(stream)

def get_symbols():
    '''
    Returns a list of all symbols defined in the config file.
    '''
    return get_config()['symbols']

def get_time_frames():
    '''
    Returns a list of dicts of all timeframes with timedelta params defined in the config file.
    '''
    return get_config()['time_frames']

def get_time_frame_names():
    '''
    Returns a list of all timeframes without additional information defined in the config file.
    '''
    return list(map(lambda x: x['name'], get_config()['time_frames']))

def get_symbols_x_time_frames():
    '''
    Returns a list of tuples containing every combination of symbols and timeframes.
    '''
    return flatten([list(zip(cycle([symbol]), get_time_frame_names())) for symbol in get_symbols()])

def get_time_frame(time_frame: str):
    return list(filter(lambda x: x['name'] == time_frame, get_time_frames()))[0]

def get_timedelta_for_time_frame(time_frame: str):
    return timedelta(**get_time_frame(time_frame)['timedelta'])

def needs_history(symbol: str, time_frame: str) -> bool:
    '''
    Checks if global start date is present and if -500 timeframes exist.
    If errors exist in between this function is useless.
    '''
    pass

def get_sql_connection() -> str:
    '''
    Returns a mysql connection string for the mysql db defined in .env for usage with e.g. pandas.
    '''
    host = os.getenv('DB_HOST')
    port = int(os.getenv('DB_PORT'))
    db = os.getenv('DB_DATABASE')
    user = os.getenv('DB_USERNAME')
    pw = os.getenv('DB_PASSWORD')

    return f'mysql://{user}:{pw}@{host}:{port}/{db}'

def to_df(data, symbol, time_frame) -> pd.DataFrame:
    df = pd.DataFrame(data, columns=['mts', 'open', 'high', 'low', 'close', 'volume'])
    df['symbol'] = symbol
    df['time_frame'] = time_frame

    return df