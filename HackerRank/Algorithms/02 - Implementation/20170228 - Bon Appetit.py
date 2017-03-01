# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/bon-appetit
"""

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
costs = map(int,raw_input().strip().split(' '))
charge = int(raw_input().strip())

costs.remove(costs[k])
if sum(costs)/float(2) == float(charge):
    print 'Bon Appetit'
else:
    print int(float(charge) - sum(costs)/float(2))