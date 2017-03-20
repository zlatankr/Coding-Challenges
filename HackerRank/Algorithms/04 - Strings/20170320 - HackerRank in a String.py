# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/hackerrank-in-a-string
"""

#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip().lower()
    h = 'hackerrank'
    h2 = 0
    ix = 0
    for i in h:
        h2 += 1
        if i in s[ix: len(s)]:
            ix += s[ix: len(s)].index(i) + 1
            if ix > len(s) and h2 != len(h):
                print 'NO'
                break
            elif h2 == len(h):
                print 'YES'
        else:
            print 'NO'
            break