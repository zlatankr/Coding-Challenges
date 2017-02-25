# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 15:13:00 2016

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

# Obtain leap and normal years composed of each day of the month.

leap_year = (range(1,32)+range(1,30)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+\
         range(1,32)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+range(1,32))

normal_year = (range(1,32)+range(1,29)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+\
         range(1,32)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+range(1,32))

# Combine year and day of month for every year in 1900-2000

calendar = []
for i in xrange(1900, 2001):
    if str(i)[-2:] == '00' and i % 400 == 0:
        calendar.append(zip(list([str(i)])*len(leap_year), list(leap_year)))
    elif str(i)[-2:] == '00':    
        calendar.append(zip(list([str(i)])*len(normal_year), list(normal_year)))
    elif i % 4 == 0:
        calendar.append(zip(list([str(i)])*len(leap_year), list(leap_year)))
    else:
        calendar.append(zip(list([str(i)])*len(normal_year), list(normal_year)))

# Flatten out our nested list
        
flat = [i for z in calendar for i in z]

# Add days of week to our calendar. We are fortunate that the total is divisible by seven.

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekdays = int((float(len(flat))/7))*week

matched = zip(flat, weekdays)

# Get a subset of the years that the question asks about

subset = [i for i in matched[365:]]

# Count the number of Sundays falling on the first of a month using our final list

counts = 0
for i in range(len(subset)):
    if subset[i][1] == 'Sunday' and subset[i][-2][1]==1:
        counts +=1
        print subset[i]
    
print counts 
    