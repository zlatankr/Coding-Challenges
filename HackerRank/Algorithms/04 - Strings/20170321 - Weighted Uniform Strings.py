# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/weighted-uniform-string
"""
#!/bin/python

import sys


s = raw_input().strip()
n = int(raw_input().strip())

from collections import Counter

nums = [ord(s[0])-96]

for i in range(1, len(s)):
    if s[i] == s[i-1]:
        nums.append(nums[-1]+(ord(s[i])-96))
    else:
        nums.append(ord(s[i])-96)
nums = set(nums)    
for a0 in xrange(n):
    x = int(raw_input().strip())
    if x in nums:
        print 'Yes'
    else:
        print 'No'