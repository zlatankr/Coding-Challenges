# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 14:57:38 2017

@author: User
"""

#!/bin/python

import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

print "%.6f" % (sum([int(i>0) for i in arr])/float(n))
print "%.6f" % (sum([int(i<0) for i in arr])/float(n))
print "%.6f" % (sum([int(i==0) for i in arr])/float(n))