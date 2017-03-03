# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/append-and-delete
"""
#!/bin/python

import sys


s = raw_input().strip()
t = raw_input().strip()
k = int(raw_input().strip())
lens = len(s)
lent = len(t)
samesies = True
matches = 0
for ix in range(min(lent, lens)):
    if s[ix] == t[ix]:
        matches += 1
    else:
        break
if s != t:
    equal = lens + lent - 2*matches
    if equal == k:
        print 'Yes'
    if equal > k:
        print 'No'
    if equal < k:
        if (k - equal) <= 2*matches and (k - equal) % 2 == 0:
            print 'Yes'
        elif (k - equal) > 2*matches:
            print 'Yes'
        else:
            print 'No'
else:
    if k <= 2*matches and k % 2 == 0:
        print 'Yes'
    elif k > 2*matches:
        print 'Yes'