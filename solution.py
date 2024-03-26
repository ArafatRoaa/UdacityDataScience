import time
import pandas as pd
import numpy as np

def validateCity(xcity):
    cities = ['chicago','washington','new york']
    return xcity in cities

######

def validateMonth(xmonth):
    months = ['1','2','3','4','5','6'] 
    return xmonth in months

######

def validateDay(xday):
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday'] 
    return xday in days

######

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

######

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    # filter by month if applicable
    if month != 'all':
        # filter by month to create the new dataframe
        df = df[df['month'] == int(month)]
        
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday','sunday']
        day = days.index(day)
        df = df[df['day_of_week'] == int(day)]
    
    return df

######

def main():
    city=''
    month='all'
    day = 'all'
    
    print('Welcome To The Ultimate Solution!')
    while True:
        city = input('Which State Would You Like To Observe? Chicago, Washington ot New York? ').lower()
        if not validateCity(city):
            print('Please Enter A Valid State ')
        else:
            break
    
    filters = input('Would You Like To Filter The Data By Month, Day, Both or None? ').lower()
    if filters == 'month':
        while True:
            month = input('Which Month? Enter 1 for Jan, 2 for Feb, etc.. ').lower()
            if not validateMonth(month):
                print('Please Enter A Valid Month Number ')
            else: 
                break
    elif filters == 'day':
        while True:
            day = input('Which Day? Saturday, Sunday, Monday? etc.. ').lower()
            if not validateDay(day):
                print('Please Enter A Valid Day ')
            else: 
                break
    elif filters == 'both':
        while True:
            month = input('Which Month? Enter 1 for Jan, 2 for Feb, etc.. ') .lower()
            if not validateMonth(month):
                print('Please Enter A Valid Month Number ')
            else: 
                break
        while True:
            day = input('Which Day? Saturday, Sunday, Monday? etc.. ').lower()
            if not validateDay(day):
                print('Please Enter A Valid Day ')
            else: 
                break
            
    print(city,month,day)
    print(load_data(city,month,day).head())
######

main()
            
        