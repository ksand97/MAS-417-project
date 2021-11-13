import time
import datetime
from numpy.lib.function_base import average
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st

    

def year():
    
    # Setter inn ønskene paramtere
    ticker = input("Shortname:" )
    #ticker = 'TSLA'

    print("Which year? 20XX?: ")
    year = int(input())
    #myFunction(year)
    print("From which month in number?:" )
    month = int(input())
    #print("Day: ")
    #day = input()
    #print("Hour: ")
    #hour = input()
    #print("Minutes: ")
    #minutes = input()

    #period1 = int(time.mktime(datetime.datetime(2020, 11, 1, 23, 59).timetuple()))
    period1 = int(time.mktime(datetime.datetime(year, month, 1, 1, 1).timetuple()))

    #print("Year end: ")
    year_added = int(1)
    year_end = year + year_added
    #print("Mounth end:" )
    month_added = int(1)
    month_end = month + month_added
    #print("Day end: ")
    #day_end = input()
    #print("Hour end: ")
    #hour_end = input()
    #print("Minutes end: ")
    #minutes_end = input()
    period2 = int(time.mktime(datetime.datetime(year_end, month_end, 1, 1, 1).timetuple()))
    #period2 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
    #period2 = int(time.mktime(dateToday.timetuple()) #If Yes, set todays date
    #interval = input("Enter 1mo, 1d or 1m: ")
    interval = '1mo' # 1d, 1m


    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


    df = pd.read_csv (query_string, usecols=['Date', 'Close'])
    print(df)
    df_close_as_np = df['Close'].to_numpy()
    df_as_np = df.to_numpy()
    
    #print(df_as_np)
    print((len(df_as_np)))
    #x = np.arange(0, len(df_as_np))
    #plt.plot(x, df_close_as_np)
    #plt.show()
    Y = df_close_as_np
    #print(Y)
    return(Y)
    

def month():
    
    # Setter inn ønskene paramtere
    ticker = input("Shortname:" )
    #ticker = 'TSLA'

    print("Which year 20XX?: ")
    year = int(input())
    #myFunction(year)
    print("From which month in number?:" )
    month = int(input())
    print("From which day in number?: ")
    day = int(input())
    #print("Hour: ")
    #hour = input()
    #print("Minutes: ")
    #minutes = input()

    #period1 = int(time.mktime(datetime.datetime(2020, 11, 1, 23, 59).timetuple()))
    period1 = int(time.mktime(datetime.datetime(year, month, day, 1, 1).timetuple()))

    #print("Year end: ")
    #year_added = int(1)
    year_end = year #+ year_added
    #print("Mounth end:" )
    month_added = int(1)
    month_end = month + month_added
    #print("Day end: ")
    #day_added = int(1)
    day_end = day
    #print("Hour end: ")
    #hour_end = input()
    #print("Minutes end: ")
    #minutes_end = input()
    period2 = int(time.mktime(datetime.datetime(year_end, month_end, day_end, 1, 1).timetuple()))
    #period2 = int(time.mktime(datetime.datetime(2021, 11, 1, 23, 59).timetuple()))
    #period2 = int(time.mktime(dateToday.timetuple()) #If Yes, set todays date
    #interval = input("Enter 1mo, 1d or 1m: ")
    interval = '1d' # 1d, 1m
    #interval = '1mo' # 1d, 1m, 1wk, 1h. With 1m, 5m, 15m, 30m or 90m. 1h. 1d or 5d. 1wk. 1mo or 3mo.

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


    df = pd.read_csv (query_string, usecols=['Date', 'Close'])
    #print(df)
    df_close_as_np = df['Close'].to_numpy()
    df_as_np = df.to_numpy()
    #print(df_as_np)
    #print((len(df_as_np)))
    x = np.arange(0, len(df_as_np))
    #print(x)
    #plt.plot(x, df_close_as_np)
    #plt.show()
    
    Y_x = df_close_as_np
    #print(Y_x)
    
    Y0 = Y_x[0]
    Y1 = st.mean([Y_x[0], Y_x[1]]) #Finding the averge
    Y2 = st.mean([Y_x[2], Y_x[3]])
    Y3 = st.mean([Y_x[4], Y_x[4]])
    Y4 = st.mean([Y_x[5], Y_x[6]])
    Y5 = st.mean([Y_x[7], Y_x[8]])
    Y6 = st.mean([Y_x[9], Y_x[10]])
    Y7 = st.mean([Y_x[11], Y_x[12]])
    Y8 = st.mean([Y_x[13], Y_x[14]])
    Y9 = st.mean([Y_x[15], Y_x[16]])
    Y10 = st.mean([Y_x[17], Y_x[18]])
    Y11 = Y_x[18]
    
    Y = [Y0, Y1, Y2, Y3, Y4, Y5, Y6, Y7, Y8, Y9, Y10, Y11]
    x_Y = np.arange(0, len(Y))
    #print(x_Y)
    #print(Y)
    
    return(Y)

def choose():

    print("Which periode are you looking for? \n" "Enter: year or month in letters")
    question_period = input()
    
    #Should be set in a while loop, if insertwrong only goen through ones
    if question_period == ("year"):
        print("You have choosed year")
        Y = year()
        print(Y)
        return (Y)
        #Go go to function with input for year
    elif question_period == ("month"):
        print("You have choosed month")
        Y = month()
        print(Y)
        return (Y)
    #Go to function with input for year and mounth. Limits for day and so on.
    else :
        print("Insert wrong")
        return
    


#if __name__ == "__main__":
Y = choose()
    
    #year(df_as_numpy)
#Y = choose()


print (Y)
#return function for start 

#Sett opp en if, ikke 12 punkter, start på nytt og print "Ugylding XX for akje". 
# "(len(df_as_np)"

#Y = month()
#print(Y)
print("Finnished")


#Y = year()
#Y = month()