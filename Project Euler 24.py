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
import math

math.factorial(10)/math.factorial(10-10) # there are 3628800 permutations

numbers = range(0, 10)


start = 9876543210
count = 1
spot = 8

a = ['a', 'b', 'c']

def all_perms(elements):
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]

count = 1
for i in xrange(9876543210, 0, -1):
    if len(set(str(i))) < len(str(i)):
        pass
    else:
        count += 1
    if count == 628802:
        print 'number is', i
        break

43210
    
def perms(items):
    if len(items) <= 1:
        return items[0]
    else:
        for i in items:
            print i, perms(items[:items.index(i)]+items[items.index(i)+1:])
    

    
    
    
    