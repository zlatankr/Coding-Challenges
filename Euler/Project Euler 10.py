# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:38 2015

@author: zlatan.kremonic
"""


# 10
import timeit
"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""


def Prime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

def Num_Ten(a): # i gave up on this one b/c it was too slow
    start_t = timeit.default_timer()
    z = []
    for i in xrange(2,a):
        if len(str(i)) > 1 and str(i)[-1:] in ('0','2','4','5','6','8'):
            continue
        elif Prime(i) == True:
            z.append(i)
    print 'Runtime > ', timeit.default_timer() - start_t, ' seconds'
    print sum(z)
    return
