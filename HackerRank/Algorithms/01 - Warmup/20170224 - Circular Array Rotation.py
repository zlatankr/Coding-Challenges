# -*- coding: utf-8 -*-
"""
Problem: 
https://www.hackerrank.com/challenges/circular-array-rotation
"""

#!/bin/python

import sys


n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))


while k > 0:
    (a.insert(0,a[-1]))
    a.pop()
    k -= 1

for a0 in xrange(q):
    m = int(raw_input().strip())
    print a[m]