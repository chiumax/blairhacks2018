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
import cryptocompare

def getStockHistory(name,itrval,amount=100):
    '''
    returns a list of most recent 100 values for the given stock (abbriviated) and interval 
    this takes the average of the high and low values
    intervals options are: 'minute','day','week','month'
    '''
    ts = TimeSeries(key='C5VMXSQYDFRMISJ2', output_format='pandas')
    if itrval=='minute':data= ts.get_intraday(symbol=name,interval='1min', outputsize=amount)[0]
    elif itrval=='day':data=ts.get_daily(name)[0]
    elif itrval=='week':data=ts.get_weekly(name)[0]
    elif itrval=='month':data=ts.get_monthly(name)[0]
    avg=[]
    for i in range(len(data['2. high'])):
        avg.append((data['2. high'][i]+data['3. low'][i])/2)
    return avg

def getStock(name):
    '''
    Returns the current number value of the stock given
    '''
    ts = TimeSeries(key='C5VMXSQYDFRMISJ2', output_format='pandas')
    data, meta_data = ts.get_intraday(symbol=name,interval='1min', outputsize=1)
    return data['4. close'][-1]
    
def getCrypto(name):
    '''
    Returns the current number value of cryptocurrency given
    '''
    return cryptocompare.get_price(symbol,curr='USD')['ETH']['USD']

def getCryptoHistory(name,itrval):
    '''
    returns a list of most recent 100 values for the given cryptocurrency(abbrieviated) and interval
    this takes the average of the high and low values
    intervals options are: 'minute','hour','day','week','month'
    '''
    url = 'https://min-api.cryptocompare.com/data/histominute?fsym={}&tsym={}&limit={}&aggregate={}'.format(name.upper(),'USD', 100,1)
    page = requests.get(url)
    data = page.json()['Data']
    df = pd.DataFrame(data)
    df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
    avg=[]
    for i in range(len(df['high'])):
        avg.append((df['high'][i]+df['low'][i])/2)
    return avg
