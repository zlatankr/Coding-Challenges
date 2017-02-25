# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:37 2015

@author: zlatan.kremonic
"""


# 7
import timeit
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

def lazy_range(n):
    i = 2
    while i < n:
        yield i
        i += 1

def Prime(x):
    for i in lazy_range(x):
        if x % i == 0:
            return False
    return True

def Num_Seven(a):
    start_t = timeit.default_timer()
    z = 0
    b = 2
    while z < a:
        if Prime(b) == True:
            z += 1
        b += 1
    print 'Runtime > ', timeit.default_timer() - start_t, ' seconds'
    print b - 1
    print z
    return

