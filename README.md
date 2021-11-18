# Crypocurrencies OHLC Data Microservice
This service uses [ccxt](https://github.com/ccxt/ccxt) to obtain price data for the currency pairs ('symbols') defined in the `config.yml`.

The current version utilizes the Binance API for price data partly as a compromise between number of available symbols and trading volume, but mainly because of the loose rate limiting which allows to obtain a lot of data in a comparatively short amount of time. With low effort this can be changed to other exchanges or even modified to obtain data from several exchanges at the same time.

## Prequesites

To write the data to a MySql DB, a table `candles` should be initialized externally with the columns 
```
open: double
high: double
low: double
close: double
volume: double
symbol: string
timeframe: string
```
and an auto-incementing unsigned int pk.

The connection data for the DB are to be specified in a `.env` file in the project root. You find a `.env.example` file in the root directory.

To define symbols and timeframes feel free to modify the `config.yml` also in the root directory. Errors resulting from symbols being not available at a certain exchange are currently not catched.

### Dependencies
Make sure you have python >= 3.6 installed.

Then simply run
```
pip install requirements.txt
```

## Getting historical data
To fill your table with the defined data, simply run:
```
python src/historical.py
```
## Getting live data
Not implemented yet!
