import time
import pandas as pd
import numpy as np

def validateCity(xcity):
    cities = ['chicago','washignton','new york']
    return xcity in cities

def validateMonth(xmonth):
    months = ['1','2','3','4','5','6','7','8','9','10','11','12'] 
    return xmonth in months

def validateDay(xday):
    days = ['saturday','sunday','monday','tuesday','wedensday','thursday','friday'] 
    return xday in days

def main():
    city='',
    month=''
    day = ''
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
    
main()
            
        