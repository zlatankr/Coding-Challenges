# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/migratory-birds?h_r=next-challenge&h_v=zen
"""

#!/bin/python

import sys


n = int(raw_input().strip())
types = map(int, raw_input().strip().split(' '))

from collections import Counter

types.sort()
a = Counter(types)

print list(a.viewkeys())[list(a.viewvalues()).index(max(a.viewvalues()))]