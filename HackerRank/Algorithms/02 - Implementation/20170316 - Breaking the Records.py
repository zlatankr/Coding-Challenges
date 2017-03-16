# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/breaking-best-and-worst-records
"""

#!/bin/python

import sys


n = int(raw_input().strip())
score = map(int, raw_input().strip().split(' '))
min_count = 0
max_count = 0
for i in range(1, len(score)):
    if score[i] < min(score[:i]):
        min_count += 1
    elif score[i] > max(score[:i]):
        max_count += 1
print max_count, min_count