# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:33 2015

@author: zlatan.kremonic
"""


# 3
import timeit
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

def lazy_range(n):
    i = 2
    while i < n:
        yield i
        i += 1

def lazy_range2(n):
    i = n
    while i > 0:
        yield i
        i -= 1

def Prime(x):
    for i in lazy_range(x):
        if x % i == 0:
            return False
    return True

def Num_three(x):
    for i in lazy_range(x):
        if x % i == 0 and Prime(x/i) == True:
            print x/i
            break
    return

Num_three(13195)

Num_three(600851475143)

