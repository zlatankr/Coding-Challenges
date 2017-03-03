# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/find-digits
"""
#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())
    total = 0
    for i in [int(z) for z in str(n)]:
        if i == 0:
            pass
        elif n % i == 0:
            total += 1
    print total