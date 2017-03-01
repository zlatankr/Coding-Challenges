# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/plus-minus
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print "%.6f" % (sum([int(i>0) for i in arr])/float(n))
print "%.6f" % (sum([int(i<0) for i in arr])/float(n))
print "%.6f" % (sum([int(i==0) for i in arr])/float(n))