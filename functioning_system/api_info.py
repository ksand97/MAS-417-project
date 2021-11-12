import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def request():


    # Setter inn ønskene paramtere
    ticker = 'TSLA'
    period1 = int(time.mktime(datetime.datetime(2020, 11, 1, 23, 59).timetuple()))
    period2 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
    interval = '1mo' # 1d, 1m


    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'

    # henter X akse og Y akseverdier
    df = pd.read_csv (query_string, usecols=['Date', 'Close'])

    df_close_as_np = df['Close'].to_numpy()
    df_as_np = df.to_numpy()

    # 3D plot ved oppgitt XYZ som np.array ( bytte ut X og Y np.array til Date and Close verdiene fra apiet)
    #X = np.arange(0,len(df_close_as_np))

    Y = df_close_as_np
    

    return (Y)




Y = request()
