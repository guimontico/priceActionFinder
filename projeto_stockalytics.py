#!/usr/bin/env python

#import libraries
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
from pandas import DataFrame

#set the key and the output format 
ALPHA_VANTAGE_API_KEY = 'FAMIMUBSM0W9GBRE'
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

#selected symbol
intraday_data, data_info = ts.get_intraday(symbol='EURUSD', outputsize='full', interval='60min')

#sort from older to newest
intraday_data = intraday_data.sort_values(by='date', ascending=True)

intraday_data.columns = ['Open', 'High', 'Low', 'Close', 'volume']

intraday_data = intraday_data.reset_index()

EURUSD_60min = pd.read_csv('data/eurusd.csv')

EURUSD_60min = EURUSD_60min.drop(['Unnamed: 0'], axis=1)

EURUSD_60min = EURUSD_60min.append(intraday_data, ignore_index=True)

EURUSD_60min = EURUSD_60min.drop_duplicates()

EURUSD_60min = EURUSD_60min.drop_duplicates(subset=['Open', 'High', 'Low', 'Close'], keep='first')

for i, row in EURUSD_60min.iterrows():
    EURUSD_60min.at[i,'date'] = pd.Timestamp(row.date)

EURUSD_60min = EURUSD_60min.sort_values(by='date', ascending=True)

EURUSD_60min.to_csv('data/eurusd.csv', index=False)
