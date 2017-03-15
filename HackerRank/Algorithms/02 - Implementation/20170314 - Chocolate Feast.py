# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/chocolate-feast
"""
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,c,m = raw_input().strip().split(' ')
    n,c,m = [int(n),int(c),int(m)]
    count = 0
    wrappers = 0
    while n >= c or wrappers >= m:
        count += n/c
        wrappers += n/c
        n -= (n/c)*c
        count += wrappers/m
        wrappers -= (wrappers/m)*(m-1)  

    print count 