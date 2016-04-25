# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 18:56:34 2016

@author: zlatan.kremonic
"""

import timeit

def num_sixteen():
    start_t = timeit.default_timer()
    print sum([int(char) for char in str(2**1000)])
    print timeit.default_timer() - start_t
    return