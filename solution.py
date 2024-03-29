import time
import calendar
import pandas as pd
import numpy as np

def cleanData(dataFrame):
    if 'Gender' in dataFrame:
        return dataFrame.dropna(subset=['Gender', 'Birth Year'])
    return dataFrame

######

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

def rowChoice(xchoice):
    choices = ['yes', 'no'] 
    return xchoice in choices

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
    # to check which city is choosen, to determine if there will be extra info or not - ex: gender
    if city == 'washington':
        extra_info_flag = False
    else:
        extra_info_flag = True
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    # clean data
    df = cleanData(df)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month,day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    df['start_hour'] = df['Start Time'].dt.hour
    
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
    
    return df,extra_info_flag

######

def calculations(dataFrame,extra_info_flag):
    
    print('Popular Month : ' + str(calendar.month_name[dataFrame['month'].mode()[0]]))
    print('Popular Day : ' + str(calendar.day_name[dataFrame['day_of_week'].mode()[0]]))
    print('Popular Start Hour : ' + str(dataFrame['start_hour'].mode()[0]))

    print('Popular Start Station : ' + str(dataFrame['Start Station'].mode()[0]))
    print('Popular End Station : ' + str(dataFrame['End Station'].mode()[0]))
    # created a new column to get the combination of the stations
    dataFrame['Station Combination'] = 'Start St -> ' + dataFrame['Start Station'] + '\n End St -> ' + dataFrame['End Station']
    print('Popular Stations Combinarion : ' + str(dataFrame['Station Combination'].mode()[0]))
    
    print('Total Duration : ' + str(round(dataFrame['Trip Duration'].sum(),3)))
    print('Avg Duration : ' + str(round(dataFrame['Trip Duration'].mean(),3)))
    
    print(dataFrame['User Type'].value_counts().reset_index().to_string(index=False))
    # if the file has extra columns AKA not washington
    if extra_info_flag: 
        gender_count = dataFrame['Gender'].value_counts().reset_index()
        min_birth = int(dataFrame['Birth Year'].min())
        max_birth = int(dataFrame['Birth Year'].max())
        common_birth = int(dataFrame['Birth Year'].mode()[0])
        
        print(gender_count.to_string(index=False))
        print('Earliest Birth Year : ' + str(min_birth))
        print('Recent Birth Year : ' + str(max_birth))
        print('Pobular Birth Year : ' + str(common_birth))
    else:
        print('Gender Count : Not Provided')
        print('Earliest Birth Year : Not Provided')
        print('Recent Birth Year : Not Provided')
        print('Pobular Birth Year : Not Provided')
        
######

def display_rows(df, start_index):
    end_index = start_index + 5
    print(df.iloc[start_index:end_index])
    
######

def main():
    city=''
    month='all'
    day = 'all'
    start_index = 0
    
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
            month = input("Which Month? Enter 1 for Jan, 2 for Feb, etc.. (only 'til June) ").lower()
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
            
    resultDF,extra_info_flag = load_data(city,month,day)
    
    print(calculations(resultDF,extra_info_flag))
    
    while(True):
        while(True):
            choice = input('Do You Want To Observe 5 Rows of The DataFrame? Yes/No? ')
            if not rowChoice(choice.lower()):
                print('Please Enter A Valid Choice ')
            else: 
                break
            
        if choice.lower() == 'yes':
            if start_index >= len(resultDF):
                print("End of DataFrame reached.")
                break
            display_rows(resultDF, start_index)
            start_index = start_index + 5
        else :
            print('End of Program!')
            break
            
    
######

main()
            
        