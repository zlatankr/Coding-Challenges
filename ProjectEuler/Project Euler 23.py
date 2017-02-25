# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 10:44:01 2016

A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 
1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of 
two abundant numbers. However, this upper limit cannot be reduced any further 
by analysis even though it is known that the greatest number that cannot be 
expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers.
"""

import itertools
import timeit




def divisors(n):
        divs = [1]
        for i in xrange(2, int(n**(float(1)/2))+1):
            if n % i == 0:
                divs.append(i)
                divs.append(n/i)
        return list(set(divs))


def number_23():
    start = timeit.default_timer()       
    
    # make a list of all the abundant numbers
    abundant_numbers = []
    for i in xrange(2, 28123):
        if sum(divisors(i)) > i:
            abundant_numbers.append(i)
    
    # make a list of all the combinations of two abundant numbers
    pairs = []        
    for subset in itertools.combinations_with_replacement(abundant_numbers, 2):
        pairs.append(subset)
    
    # find the sum of each combination of abundant numbers
    pair_sums = []
    for i in pairs:
        if sum(i) < 28124:
            pair_sums.append(sum(i))
    
    # dedupe the list of sums
    ded = list(set(pair_sums))
    
    # remove the sums from a list of all the integers from 1 to 28123        
    numbers = range(1, 28124)
    
    for i in ded:
        if i in numbers:
            numbers.remove(i)
    
    print sum(numbers)
    print timeit.default_timer() - start, 'seconds'
    return
