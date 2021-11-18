from typing import List, Tuple
from datetime import datetime


def get_new(symbol: str, time_frame: str) -> List[Tuple[datetime, float, float, float, float, float]]:
    '''
    Returns the most recent 500 rows of OHLC data for the given symbol and timeframe.
    '''
    pass