# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/taum-and-bday
"""

#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    b,w = raw_input().strip().split(' ')
    b,w = [long(b),long(w)]
    x,y,z = raw_input().strip().split(' ')
    x,y,z = [long(x),long(y),long(z)]
    if x + z < y:
        print x*b + (x + z)*w
    elif y + z < x:
        print (y + z)*b + (y)*w
    else:
        print x*b + y*w