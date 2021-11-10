import time
import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def request():
    

    # Setter inn ønskene paramtere
    ticker = input("Shortname:" )
    #ticker = 'TSLA'
    print("Year: ")
    year = input()
    print("Mounth:" )
    mounth = input()
    print("Day: ")
    day = input()
    print("Hour: ")
    hour = input()
    print("Minutes: ")
    minutes = input()

    #period1 = int(time.mktime(datetime.datetime(2020, 11, 1, 23, 59).timetuple()))
    period1 = int(time.mktime(datetime.datetime(int(year), int(mounth), int(day), int(hour), int(minutes)).timetuple()))

    print("Year end: ")
    year_end = input()
    print("Mounth end:" )
    mounth_end = input()
    print("Day end: ")
    day_end = input()
    print("Hour end: ")
    hour_end = input()
    print("Minutes end: ")
    minutes_end = input()
    period2 = int(time.mktime(datetime.datetime(int(year_end), int(mounth_end), int(day_end), int(hour_end), int(minutes_end)).timetuple()))
    #period2 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
    #period2 = int(time.mktime(dateToday.timetuple()) #If Yes, set todays date
    interval = input("Enter 1mo, 1d or 1m: ")
    #interval = '1mo' # 1d, 1m


    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


    df = pd.read_csv (query_string, usecols=['Date', 'Close'])
    print(df)
    df_close_as_np = df['Close'].to_numpy()

    df_as_np = df.to_numpy()
    
    Y = df_close_as_np
    print(df_as_np)
    print((len(df_as_np)))
    x = np.arange(0, len(df_as_np))
    plt.plot(x, df_close_as_np)
    plt.show()
    return (Y)



Y = request()
