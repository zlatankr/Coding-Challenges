# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/library-fine
"""

#!/bin/python

import sys


d1,m1,y1 = raw_input().strip().split(' ')
d1,m1,y1 = [int(d1),int(m1),int(y1)]
d2,m2,y2 = raw_input().strip().split(' ')
d2,m2,y2 = [int(d2),int(m2),int(y2)]

if y1 < y2:
    print 0
elif m1 < m2 and y1 == y2:
    print 0
else:
    print max(15*(d1-d2), 500*(m1-m2), 10000*(min(y1-y2, y1/y2)))