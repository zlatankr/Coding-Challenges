# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 15:31:55 2016

A permutation is an ordered arrangement of objects. For example, 3124 is one 
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations 
are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import timeit

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

def number_24():
    start = timeit.default_timer()
    a = list(all_perms(str(9876543210)))
    a.sort()
    print timeit.default_timer() - start, 'seconds'
    print a[999999]
    return