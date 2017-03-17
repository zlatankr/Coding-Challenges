# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/reduced-string
"""
s = raw_input().strip()

a = 1
while a == 1:
    lens = len(s)
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            s = s[:i-1]+s[i+1:]
            break
    if len(s) == lens:
        a -= 1
if len(s) == 0:
    print 'Empty String'
else:
    print s