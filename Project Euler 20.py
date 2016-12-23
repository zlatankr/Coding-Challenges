# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 10:07:31 2016

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

# We use a simple recursion functionto get our answer:
    
def number_20(n):
    def fact(n):
        if n == 0:
            return 1
        else:
            return n * fact(n-1)
    return sum([int(i) for i in str(fact(n))])
        

