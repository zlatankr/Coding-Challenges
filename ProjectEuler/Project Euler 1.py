# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 16:22:25 2015

@author: zlatan.kremonic
"""

# 1
import timeit
""" 
If we list all the natural numbers below 10 that are multiples of 3 or 5
, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""
import numpy as np

def Num_one(x):
    z = []
    for i in range(1,x):
        if i % 3 == 0:
            z.append(i)
        elif i % 5 == 0:
            z.append(i)
    return np.sum(z)

Num_one(1000)
