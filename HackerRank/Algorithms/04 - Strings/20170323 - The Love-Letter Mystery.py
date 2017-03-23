# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/the-love-letter-mystery
"""
n = int(raw_input())
for j in range(n):
    s = raw_input().strip()
    a = len(s)/2
    print sum([abs(ord(s[i])-ord(s[::-1][i])) for i in range(a)])