# -*- coding: utf-8 -*-
"""
Link to challenge: 

https://www.hackerrank.com/challenges/mini-max-sum
"""

#!/bin/python

import sys


a,b,c,d,e = raw_input().strip().split(' ')
a,b,c,d,e = [int(a),int(b),int(c),int(d),int(e)]

nums = [a, b, c, d, e]
nums.sort()
mins = sum(nums[:4])
nums.sort(reverse = True)
maxs = sum(nums[:4])
print mins, maxs