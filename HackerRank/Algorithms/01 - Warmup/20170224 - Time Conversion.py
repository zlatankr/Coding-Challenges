"""
https://www.hackerrank.com/challenges/time-conversion
"""

#!/bin/python

import sys


time = raw_input().strip()

if time[-2:] == 'AM' and time[:2] == '12':
    print '00'+time[2:-2]
elif time[-2:] == 'PM' and time[:2] == '12':
    print '12'+time[2:-2]
elif time[-2:] == 'AM':
    print time[:-2]
else:
    print str(int(time[:2])+12)+time[2:-2]