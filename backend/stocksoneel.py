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
    '''
    returns a list of most recent 100 values for the given stock (abbriviated) and interval 
    this takes the average of the high and low values
    intervals options are: 'minute','day','week','month'
    '''
    ts = TimeSeries(key='C5VMXSQYDFRMISJ2', output_format='pandas')
    if itrval=='minute':data, meta_data = ts.get_intraday(symbol=name,interval='1min', outputsize='full')
    elif itrval=='day':data=ts.get_daily(name,100)[0]
    elif itrval=='week':data=ts.get_weekly(name,100)[0]
    elif itrval=='month':data=ts.get_monthly(name,100)[0]
    for i in range(len(data['2. high'])):
        avg.append((data['2. high'][i]+data['3. low'])/2)
    return avg

def BCprice(symbol, comparison_symbols=['USD'], exchange=''):
    url = 'https://min-api.cryptocompare.com/data/price?fsym={}&tsyms={}'\
            .format(symbol.upper(), ','.join(comparison_symbols).upper())
    if exchange:
        url += '&e={}'.format(exchange)
    page = requests.get(url)
    data = page.json()
     return data

def getCrypto(symbol,itrval):
    '''
    returns a list of most recent 100 values for the given cryptocurrency(abbrieviated) and interval
    this takes the average of the high and low values
    intervals options are: 'minute','hour','day','week','month'
    '''
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'.format(symbol.upper(),'USD', 100,1)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    avg=[]
    for i in range(len(df['high'])):
        avg.append((df['high'][i]+df['low'][i])/2)
    return avg


#print(getCrypto('BTC','day'))
#print(getStock('GOOGL',1))

