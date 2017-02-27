# -*- coding: utf-8 -*-
"""
Link to challenge:

https://www.hackerrank.com/challenges/apple-and-orange
"""

#!/bin/python

import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

print sum([int(t >= i + a >= s) for i in apple])
print sum([int(s <= i + b <= t) for i in orange])