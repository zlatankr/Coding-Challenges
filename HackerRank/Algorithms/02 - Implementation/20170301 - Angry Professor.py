# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/angry-professor
"""

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))
    if sum([1 for i in a if i <= 0]) >= k:
        print 'NO'
    else:
        print 'YES'