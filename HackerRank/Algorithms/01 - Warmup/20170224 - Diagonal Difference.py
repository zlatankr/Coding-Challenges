# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/diagonal-difference
"""

#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

diag = range(n)
print abs(sum([a[z][i] for z, i in enumerate(diag)]) - sum([a[z][i] for z, i in enumerate(diag[::-1])]))