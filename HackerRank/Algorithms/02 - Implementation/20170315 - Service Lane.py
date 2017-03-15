# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/service-lane
"""
#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]
    if min(width[i:j+1]) == 1:
        print 1
    elif min(width[i:j+1]) == 2:
        print 2
    else:
        print 3