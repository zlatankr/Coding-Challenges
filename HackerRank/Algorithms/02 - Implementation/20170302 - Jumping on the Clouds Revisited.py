# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds-revisited
"""
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
c = map(int,raw_input().strip().split(' '))

e = 100
cloud_index = 0
j = True
while j == True:
    cloud_index = (cloud_index + k) % n
    if c[cloud_index] == 0:
        e -= 1
    else:
        e -= 3
    if cloud_index == 0:
        print e
        j = False
