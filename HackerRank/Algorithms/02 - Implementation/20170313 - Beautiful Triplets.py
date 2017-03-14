# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/beautiful-triplets
"""

n, d = map(int, raw_input().strip().split(' '))
nums = map(int, raw_input().strip().split(' '))

triplets = 0
for i in nums:
    if (i - d) in nums and (i + d) in nums:
        triplets += 1
print triplets