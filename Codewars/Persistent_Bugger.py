# -*- coding: utf-8 -*-
"""
Created on Wed Dec 28 10:25:12 2016

@author: User
"""

def persistence(n):
    a = 0
    while a < 5:
        if len(str(n)) == 1:
            return a
        else:
            b = 1
            for i in range(0, len(str(n))):
                b = b*int(str(n)[i])
        n = b
        a += 1