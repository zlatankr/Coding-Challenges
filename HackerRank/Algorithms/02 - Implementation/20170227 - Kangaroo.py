# -*- coding: utf-8 -*-
"""
Link to challenge:

https://www.hackerrank.com/challenges/kangaroo
"""

x1, v1, x2, v2 = 0, 3, 4, 2

slopes = (x1-x2)>=0
intercepts = (v2-v1)>=0
if int(slopes) + int(intercepts) != 1 and (v2-v1) == 0:
    print 'YES'
elif int(slopes) + int(intercepts) != 1 and (x1-x2)%(v2-v1) == 0:
    print 'YES'
else:
    print 'NO'