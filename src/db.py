from datetime import datetime
from typing import List, Tuple
import pandas as pd
from util import get_sql_connection

# TODO unique constraint: symbol + timestamp + timeframe

def read(symbol: str, time_frame: str) -> pd.DataFrame:
    '''
    Returns all rows for given symbol and timeframe as DataFrame.
    '''
    return pd.read_sql_table('candles', get_sql_connection())

def write(df: pd.DataFrame):
    '''
    Writes data for given symbol and timeframe to DB.
    '''
    df.to_sql('candles', get_sql_connection(), if_exists='append', index=False)
