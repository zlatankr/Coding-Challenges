# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 11:06:12 2017

@author: User
"""

n, k = map(int, raw_input().strip().split(' '))
nums = map(int, raw_input().strip().split(' '))

x = list(nums[-1:])

for i in nums[:-1]:
    if any([(i + z) % k == 0 for z in x]):
        pass
    else:
        x.append(i)

print len(x)