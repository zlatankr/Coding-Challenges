# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/compare-the-triplets
"""

#!/bin/python

import sys


a0,a1,a2 = raw_input().strip().split(' ')
a0,a1,a2 = [int(a0),int(a1),int(a2)]
b0,b1,b2 = raw_input().strip().split(' ')
b0,b1,b2 = [int(b0),int(b1),int(b2)]

print int(a0>b0)+int(a1>b1)+int(a2>b2),int(a0<b0)+int(a1<b1)+int(a2<b2)