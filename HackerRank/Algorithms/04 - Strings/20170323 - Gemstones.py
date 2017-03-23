# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/gem-stones
"""

n = int(raw_input().strip())

letts = {}
for j in range(n):
    s = raw_input().strip()
    for i in set(s):
        if i in letts:
            letts[i] += 1
        else:
            letts[i] = 1
tots = 0
for i in letts:
    if letts[i] == n:
        tots += 1
print tots