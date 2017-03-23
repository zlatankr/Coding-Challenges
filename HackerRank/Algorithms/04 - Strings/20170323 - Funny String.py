# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/funny-string
"""

n = int(raw_input().strip())

for j in range(n):
    s = raw_input().strip()
    if [abs(ord(s[i]) - ord(s[i-1])) for i in range(1, len(s))] == [abs(ord(s[::-1][i]) - ord(s[::-1][i-1])) for i in range(1, len(s))]:
        print 'Funny'
    else:
        print 'Not Funny'