# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/minimum-distances
"""
#!/bin/python

import sys


n = int(raw_input().strip())
A = map(int,raw_input().strip().split(' '))

track = {}
for ix, i in enumerate(A):
    if i not in track:
        track[i] = [ix]
    else:
        track[i].append(ix)

if max([len(i) for i in track.viewvalues()]) == 1:
    print -1
else:
    j = 1000000000
    for z in track.viewvalues():
        if len(z) > 1:
            b = min([z[i]-z[i-1] for i in range(1,len(z))])
            if b < j:
                j = b
    print j