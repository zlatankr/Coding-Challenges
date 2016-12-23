# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:03:34 2016

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called 
amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def number_21():

    # first, we write a function to find all the divisors of a given number
    def divisors(n):
        divs = [1]
        for i in xrange(2, int(n**(float(1)/2))):
            if n % i == 0:
                divs.append(i)
                divs.append(n/i)
        return divs
    
    # then, we create a dict for each number under 10,000 with the sume of its proper divisors
    pairs = {}
    for i in xrange(1, 10000):
    
        pairs[i] = sum(divisors(i))

    # finally, we loop through our dict and check whether or not it's an amicable number...
    amicables = []
    for i in pairs:
        if pairs[i] < 10000 and (pairs[pairs[i]] == i) and pairs[i] <> i:
            amicables.append(i)
            amicables.append(pairs[i])
    
    # and return the sum of our amicable numbers
    return sum(set(amicables))