Udacity Datascience For All NanoDegree Final Project

This Project is Using Python 3.10 and Pandas 2.2.0

--

The project lets the user observe thee different data frames and gives out the calculations needed.

The data frames corresponds to the three .csv files with columns for each: 
 - chicago.csv : id,Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
 - new_york_city.csv : id,Start Time,End Time,Trip Duration,Start Station,End Station,User Type,Gender,Birth Year
 - washington.csv : id,Start Time,End Time,Trip Duration,Start Station,End Station,User Type

The calculations are: 

 #1 Popular times of travel (i.e., occurs most often in the start time)
    most common month
    most common day of week
    most common hour of day
 #2 Popular stations and trip
    most common start station
    most common end station
    most common trip from start to end (i.e., most frequent combination of start station and end station)
 #3 Trip duration
    total travel time
    average travel time
 #4 User info
    counts of each user type
    counts of each gender (only available for NYC and Chicago)
    earliest, most recent, most common year of birth (only available for NYC and Chicago)
    
--

To use: 
 - Clone This Repo
 - Make sure you have Python downloaded
 - Download Pandas in cmd: pip install pandas
 - run in local project cmd: python bikeshare_2.py
