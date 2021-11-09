import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Setting shortname, period and interval
ticker = 'TSLA'
period1 = int(time.mktime(datetime.datetime(2020, 11, 1, 23, 59).timetuple()))
period2 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
interval = '1mo' # 1d, 1m


query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


df = pd.read_csv (query_string, usecols=['Date', 'Close'])
print(df)
