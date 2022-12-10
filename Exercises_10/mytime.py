# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:04:55 2022

@author: Jen
"""

from datetime import datetime as dt

 
# Get the current time, returns a value like 2022-10-09 17:46:45.151666 
today = dt.now() 
print(today) 

# Get Unix time, returns a value like 1665566809.057217 
unix_epoch_time = dt.timestamp(today) 
print(unix_epoch_time)

weekday = dt.now().strftime("%A")
#print(weekday)

month = dt.now().strftime("%B")
#print(month)

date_time_now = dt.now().strftime("%A, %d. %B %Y, %I:%M:%S")


print(f"The current date and time is {date_time_now}")