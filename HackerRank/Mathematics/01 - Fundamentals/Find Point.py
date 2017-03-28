# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/find-point
"""

n = int(raw_input().strip())

for i in range(n):
    px, py, qx, qy = map(int, raw_input().strip().split(' '))
    print qx + (qx - px), qy + (qy - py)