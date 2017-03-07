# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/equality-in-a-array
"""

from collections import Counter

n = int(raw_input().strip())
nums = map(int, raw_input().strip().split(' '))

if len(nums) == 1:
    print 0
else: 
    print len(nums) - max(Counter(nums).viewvalues())
