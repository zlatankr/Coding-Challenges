# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/divisible-sum-pairs
"""
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
a = map(int,raw_input().strip().split(' '))

pairs = 0
for ix_one in xrange(n-1):
    for ix_two in xrange(ix_one+1, n):
        if (a[ix_one] + a[ix_two]) % k == 0:
            pairs += 1
print pairs