#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import libraries
from alpha_vantage.foreignexchange import ForeignExchange
from alpha_vantage.timeseries import TimeSeries
import matplotlib.pyplot as plt
import pandas as pd
from pandas import DataFrame
from google.colab import files
from datetime import datetime

from pandas_datareader import data as web
import plotly.graph_objects as go

#set the key and the output format 
ALPHA_VANTAGE_API_KEY = 'FAMIMUBSM0W9GBRE'
ts = TimeSeries(key=ALPHA_VANTAGE_API_KEY, output_format='pandas')

#selected symbol
intraday_data, data_info = ts.get_intraday(symbol='EURUSD', outputsize='full', interval='60min')

#sort from older to newest
intraday_data = intraday_data.sort_values(by='date', ascending=True)

intraday_data.columns = ['Open', 'High', 'Low', 'Close', 'volume']

EURUSD_60min = pd.read_csv('data/eurusd.csv')

EURUSD_60min = EURUSD_60min.append(intraday_data)

EURUSD_60min = EURUSD_60min.drop_duplicates()

EURUSD_60min.to_csv('data/eurusd.csv', index=False)
