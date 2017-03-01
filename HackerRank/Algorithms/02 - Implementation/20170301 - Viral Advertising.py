# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/strange-advertising
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

m = 5
i = int(raw_input().strip())
day = 1
likes = 0
while day <= i:
    likes += (m/2)
    m = (m/2)*3
    day += 1
print likes