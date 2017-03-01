# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/utopian-tree
"""

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    total_cycles = int(raw_input().strip())
    cycle = 1
    h = 1
    while cycle <= total_cycles:
        if cycle % 2 <> 0:
            h *= 2
        else:
            h += 1
        cycle += 1
    print h