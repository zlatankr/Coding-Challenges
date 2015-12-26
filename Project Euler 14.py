# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 10:20:38 2015

@author: zlatan.kremonic
"""

"""
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

import timeit

def collatz(n):
    z = [n]
    while n > 1:
        if n % 2 == 0:
            z.append(n // 2)
            n //= 2
        else:
            z.append(3 * n + 1)
            n *= 3
            n += 1
    return z

def num_fourteen(n):
    start_t = timeit.default_timer()
    a = {}
    for i in xrange(2,n):
        a[i] = len (collatz(i))
    print a
    print 'Runtime > ', timeit.default_timer() - start_t, ' seconds'
    print list(a.keys())[list(a.values()).index(max(list(a.values())))]
    return
