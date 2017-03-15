# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/the-time-in-words
"""
#!/bin/python

import sys


h = int(raw_input().strip())
m = int(raw_input().strip())
time = {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight',
        9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'quarter', 
        16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 21: 'twenty one', 
        22: 'twenty two', 23: 'twenty three', 24: 'twenty four', 25: 'twenty five', 26: 'twenty six', 
        27: 'twenty seven', 28: 'twenty eight', 29: 'twenty nine', 30: 'half'}

if m == 0:
    print time[h], 'o\' clock'
elif m == 1:
    print 'one minute past', time[h]
elif m == 15:
    print 'quarter past', time[h]
elif m == 30:
    print 'half past', time[h]
elif m < 30:
    print time[m], 'minutes past', time[h]
elif m == 45:
    print 'quarter to', time[h+1]
elif h == 12 and m > 30:
    print time[60-m], 'minutes', 'to one'
elif m == 59 and h== 12:
    print 'one minute to one'
elif m == 59:
    print 'one minute to', time[h+1]
else:
    print time[60-m], 'minutes to', time[h+1]