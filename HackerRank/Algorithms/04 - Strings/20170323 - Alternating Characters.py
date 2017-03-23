# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/alternating-characters
"""

n = int(raw_input().strip())

for j in range(n):
    s = raw_input().strip()
    print sum([1 for i in range(1, len(s)) if s[i] == s[i-1]])