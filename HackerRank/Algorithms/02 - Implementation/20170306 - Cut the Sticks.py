# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/cut-the-sticks
"""
#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

while sum(arr) > 0:
    print len(arr)
    arr = [i - min(arr) for i in arr]
    arr = [i for i in arr if i > 0]