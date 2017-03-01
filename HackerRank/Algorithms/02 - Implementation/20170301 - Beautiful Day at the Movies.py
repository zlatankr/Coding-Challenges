# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/beautiful-days-at-the-movies
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

a, b, c = map(int, raw_input().strip().split(' '))

days = 0
for i in range(a, b + 1):
    if (i - int(str(i)[::-1])) % c == 0:
        days += 1
print days