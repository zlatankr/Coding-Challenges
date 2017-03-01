# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/between-two-sets
"""

#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

amin = max(a)
bmin = min(b)

valid = []
for i in range (amin, bmin+1):
    if all([i % lower == 0 for lower in a]) and all([higher % i == 0 for higher in b]):
        valid.append(i)
print len(valid)