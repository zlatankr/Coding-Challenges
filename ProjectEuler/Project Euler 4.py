# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:36 2015

@author: zlatan.kremonic
"""


# 4
import timeit
"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of 
two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def Pal(x):
    if str(x)[::-1] == str(x):
        return True
    else:
        return False

def Num_four():   
    y = 1000000
    z = 10
    while y > z:
        if Pal(y) == True:
            s = 999
            while s > 1:
                if y % s == 0 and len(str(y//s)) == 3:
                    print y
                    print s
                    print y//s
                    return
                s -= 1
        y -= 1
    return
