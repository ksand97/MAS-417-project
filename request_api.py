import time
import datetime
from numpy.lib.function_base import average
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statistics as st


class UserInput:
    def __init__(self, year_in, month_in, day_in):
        self.year_in = year_in
        self.month_in = month_in
        self.day_in = day_in

def choose():
    
    print("Welcome! \nHere you can generate STL-files, displaying the movement of common stock prices within a given month or year!")
    Y = ""
    while Y == "":
               
        print("Choose stock (ex. TSLA, AAPL):")
        stock = input()
        print("What period do you want? Enter: y for yearly, m for monthly")
        question_period = input()
        
        if question_period == ("y"):
            print("You have chosen year")
            Y = year(stock)
            return (Y, stock)
            
        elif question_period == ("m"):
            print("You have chosen month")
            Y = month(stock)
            return (Y, stock)
        
        else :
            print("Insert wrong")
    
def year(ticker):
    
    print("Choose year (in number)? ")
    input1 = int(input())
    print("Form which month (in number)? ")
    input2 = int(input())
    
    request = UserInput(input1, input2, 1)
 
    period1 = int(time.mktime(datetime.datetime(request.year_in, request.month_in, 1, 1, 1).timetuple()))

    year_added = int(1)
    year_end = request.year_in + year_added
  
    month_added = int(1)
    month_end = request.month_in + month_added

    period2 = int(time.mktime(datetime.datetime(year_end, month_end, 1, 1, 1).timetuple()))

    interval = '1mo'

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


    df = pd.read_csv (query_string, usecols=['Date', 'Close'])
    print(df)
    df_close_as_np = df['Close'].to_numpy()
    df_as_np = df.to_numpy()
    
    x = np.arange(0, len(df_as_np))
    
    plt.plot(x, df_close_as_np)
    
    plt.savefig(ticker)

    Y = df_close_as_np
 
    return(Y)

def month(ticker):
    
    print("Choose year (in number)? ")
    input1 = int(input())
    print("Form which month (in number)? ")
    input2 = int(input())
    print("From which day (in number)? ")
    input3 = int(input())
    
    request = UserInput(input1, input2, input3)

    period1 = int(time.mktime(datetime.datetime(request.year_in, request.month_in, request.day_in, 1, 1).timetuple()))

    year_end = request.year_in
    
    month_added = int(1)
    month_end = request.month_in + month_added
    
    day_end = request.day_in
    
    period2 = int(time.mktime(datetime.datetime(year_end, month_end, day_end, 1, 1).timetuple()))
    
    interval = '1d'
    

    query_string = f'https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={period1}&period2={period2}&interval={interval}&events=history&includeAdjustedClose=true'


    df = pd.read_csv (query_string, usecols=['Date', 'Close'])
    df_close_as_np = df['Close'].to_numpy()
    df_as_np = df.to_numpy()
    print(df)
    x = np.arange(0, len(df_as_np))
    Y_x = df_close_as_np
    
    
    Y0 = Y_x[0]
    Y1 = st.mean([Y_x[0], Y_x[1]])
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
    x = np.arange(0, len(df_as_np))
    
    plt.plot(x_Y, Y)
    plt.savefig(ticker)
    
    return(Y)


result = choose()
Y = result[0]
nameofstock = result[1]