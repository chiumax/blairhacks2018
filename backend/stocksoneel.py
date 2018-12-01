'''from yahoo_finance import Share
yahoo=Share('YHOO')
print (yahoo.get_historical('2014-04-25', '2014-04-29'))
from googlefinance import getQuotes
import json
print (json.dumps(getQuotes('AAPL'), indent=2))
'''

from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import matplotlib as plt
import requests
import datetime
def getStock(name,itrval):
    # '1min', '5min', '15min', '30min', '60min'
    ts = TimeSeries(key='C5VMXSQYDFRMISJ2', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=name,interval=str(itrval)+'min', outputsize='full')
    avg=[]
    for i in range(len(data['2. high'])):
        avg.append((data['2. high'][i]+data['3. low'])/2)
    return avg

def price(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
    return data
def daily_price_historical(symbol, comparison_symbol, all_data=True, limit=100, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histoday?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    if all_data:
        url += '&allData=true'
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

def hourly_price_historical(symbol, comparison_symbol, limit=100, aggregate=1, exchange=''):
    url = 'https://min-api.cryptocompare.com/data/histohour?fsym={}&tsym={}&limit={}&aggregate={}'\
            .format(symbol.upper(), comparison_symbol.upper(), limit, aggregate)
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    return df

print(getStock('GOOGL',1))
print(daily_price_historical("BTC","USD").to_string())
print(hourly_price_historical("BTC","USD").to_string())
