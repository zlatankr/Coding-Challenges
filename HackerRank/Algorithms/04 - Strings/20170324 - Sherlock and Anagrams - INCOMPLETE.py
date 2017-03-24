# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/sherlock-and-anagrams
"""

from collections import Counter

s = 'ifailuhkqq'

for i in Counter(s):
    if Counter(s)[i] == 1:
        s = s.replace(i, '')

for ix in range(len(s)):
    tots = 1
    while tots <= len(s)/2:
        
    