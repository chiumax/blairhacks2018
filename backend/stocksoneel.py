'''from yahoo_finance import Share
yahoo=Share('YHOO')
print (yahoo.get_historical('2014-04-25', '2014-04-29'))
from googlefinance import getQuotes
import json
print (json.dumps(getQuotes('AAPL'), indent=2))
'''

from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.cryptocurrencies import CryptoCurrencies
import pandas as pd
import requests
import datetime
import cryptocompare

def getStockHistory(name,itrval):
    '''
    returns a dictionary of most recent 100 values for the given stock (abbriviated) and interval with the date
    this takes the average of the high and low values
    month returns all of the values from the start of launch
    intervals options are: 'minute','day','week','month'
    '''
    ts = TimeSeries(key='C5VMXSQYDFRMISJ2', output_format='pandas')
    if itrval=='minute':data= ts.get_intraday(symbol=name,interval='1min', outputsize=100)[0]
    elif itrval=='day':data=ts.get_daily(name)[0]
    elif itrval=='week':data=ts.get_weekly(name)[0]
    elif itrval=='month':data=ts.get_monthly(name)[0]
    vals={}
    for i in range(len(data['4. close'])):
        vals[list(data.index)[i]]=(data['4. close'][i]+data['4. close'][i])/2
    return vals

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
    returns a dictionary of most recent 100 values for the given cryptocurrency(abbrieviated) and interval with the date
    this takes the average of the high and low values
    intervals options are: 'minute','hour','day'
    '''
    if itrval=='week':
        cc = CryptoCurrencies(key='C5VMXSQYDFRMISJ2', output_format='pandas')
        data= cc.get_digital_currency_weekly(symbol=name, market='USD')[0]
        vals={}
        for i in range(len(data['4b. close (USD)'])):
            vals[list(data.index)[i]]=data['4b. close (USD)'][i]
        return vals
    elif itrval=='month':
        cc = CryptoCurrencies(key='C5VMXSQYDFRMISJ2', output_format='pandas')
        data= cc.get_digital_currency_monthly(symbol=name, market='USD')[0]
        vals={}
        for i in range(len(data['4b. close (USD)'])):
            vals[list(data.index)[i]]=data['4b. close (USD)'][i]
        return vals
    else:
        url = ('https://min-api.cryptocompare.com/data/histo'+itrval+'?fsym={}&tsym={}&limit={}&aggregate={}').format(name.upper(),'USD', 100,1)
        print(url)
        page = requests.get(url)
        data = page.json()['Data']
        df = pd.DataFrame(data)
        df['timestamp'] = [datetime.datetime.fromtimestamp(d) for d in df.time]
        vals={}
        print(len(list(df.index)))
        for i in range(len(df['high'])):
            vals[df['timestamp'][i]]=(df['high'][i]+df['low'][i])/2
        return vals
