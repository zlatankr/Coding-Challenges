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
leap_year = zip((list('1')*31+list('2')*29+list('3')*31+list('4')*30+list('5')*31+list('6')*30+\
        list('7')*31+list('8')*31+list('9')*30+list(['10'])*31+list(['11'])*30+list(['12'])*31),
        (range(1,32)+range(1,30)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+\
         range(1,32)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+range(1,32)))

normal_year = zip((list('1')*31+list('2')*28+list('3')*31+list('4')*30+list('5')*31+list('6')*30+\
        list('7')*31+list('8')*31+list('9')*30+list(['10'])*31+list(['11'])*30+list(['12'])*31),
        (range(1,32)+range(1,29)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+\
         range(1,32)+range(1,32)+range(1,31)+range(1,32)+range(1,31)+range(1,32)))

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

flat = [i for z in calendar for i in z]

week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

weekdays = int((float(len(flat))/7))*week

matched = zip(flat, weekdays)

subset = [i for i in matched[365:]]

counts = 0
for i in range(len(subset)):
    if subset[i][1] == 'Sunday' and subset[i][-2][1][1]==1:
        counts +=1
        print subset[i]
    
print counts 
    
    