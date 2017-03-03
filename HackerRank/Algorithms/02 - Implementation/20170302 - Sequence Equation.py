# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/permutation-equation
"""
n = int(raw_input().strip())
nums = map(int, raw_input().strip().split())

for ix, num in enumerate(nums):
    print nums.index(nums.index(ix + 1) + 1) + 1