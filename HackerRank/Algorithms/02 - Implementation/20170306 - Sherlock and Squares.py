# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/sherlock-and-squares
"""

def start(x):
    if x % x**(float(1)/2) == 0.0:
        return int(x**(float(1)/2))
    else:
        return int(x**(float(1)/2)) + 1

n = int(raw_input().strip())
for row in range(n):
    z = map(int, raw_input().strip().split(' '))
    print len(range(start(z[0]), int(z[1]**(float(1)/2))+1))