# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/the-hurdle-race
"""
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
height = map(int, raw_input().strip().split(' '))
if (max(height)-k) > 0:
    print max(height)-k
else: 
    print 0