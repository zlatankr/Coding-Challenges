# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:37 2015

@author: zlatan.kremonic
"""


# 6
import timeit
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of 
the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of 
the first one hundred natural numbers and the square of the sum.
"""

import numpy as np

np.square(sum(range(101))) - sum(np.square(range(101)))
