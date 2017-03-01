# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/sock-merchant
"""
#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

from collections import Counter

counts = Counter(c)
pairs = 0
for i in counts:
    pairs += counts[i]/2

print pairs