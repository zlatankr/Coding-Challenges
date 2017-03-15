# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/fibonacci-modified
"""
t1, t2, n = map(int,raw_input().strip().split())

def fib2(t1, t2, n):
    tots = [t1, t2]
    while len(tots) < n:
        tots.append(tots[-2]+tots[-1]**2)
    print tots[-1]
    return
fib2(t1, t2, n)