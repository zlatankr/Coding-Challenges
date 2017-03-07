# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/jumping-on-the-clouds
"""
#!/bin/python

import sys


n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))

ix = 0
moves = 0
while ix != len(c) - 1:
    if ix + 2 == len(c) - 1:
        moves += 1
        print moves
        ix += 2
    elif ix + 1 == len(c) - 1:
        moves += 1
        print moves
        ix += 1
    elif c[ix+2] == 0:
        moves += 1
        ix += 2
    elif c[ix+1] == 0:
        moves += 1
        ix += 1