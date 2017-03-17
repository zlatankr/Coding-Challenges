# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/two-characters
"""
#!/bin/python

import sys
from collections import Counter

s_len = int(raw_input().strip())
s = raw_input().strip()

def zz_top(s):
    if len(s) == 1:
        print 0
        return
    if len(set(s))== 1:
        print 0
        return
    c = Counter(s)
    lets = sorted(c, key=c.get, reverse=True)
    tots = [0]
    for i in range(len(lets)-1):
        for j in range(i+1, len(lets)):
            if c[lets[i]] - c[lets[j]] <= 1 and c[lets[i]] + c[lets[j]] > max(tots):
                x = [m for m in s if m in [lets[i], lets[j]]]
                if all([x[m] != x[m-1] for m in range(1, len(x))]):
                    tots.append(len(x))
    print max(tots)
    return

zz_top(s)