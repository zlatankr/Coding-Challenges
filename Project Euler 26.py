# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 12:01:08 2017

A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.

"""

"""
- Create an empty dict

- for each n in 2 to 1000:

- if n is in dict, skip to next one
    
- if 1000 is perfectly divisible by n
    - add n and 1000/n to dict with value: 0

- if number of decimals is less than 100:
    - add n to dict with value: 0
    
- Else create a function with a while loop up to 100:
    - takes one decimal at a time (equal to wherever the while loop is)
    - repeats it until we have 100 of those number
    - divides our orinal number by the new number
    - if we get a one, then that's how many repeating numbers there
    - add n to dict with vale equal to value of while loop

"""
from decimal import *

getcontext().prec = 200
decimals = {}

for i in xrange(2, 1000):
    print 'i is', i
    if i in decimals:
        pass
    elif float(1000) % i == 0:
        decimals[i] = 0
        decimals[int(float(1000)/i)] = 0
    elif len(str(Decimal(1)/Decimal(i))) > 200:
        a = 1
        while a < 201:
            print 'a is', a
            z = str(Decimal(1)/Decimal(i))[2:(2+a)]
            if int(z) == 0:
                a += 1
            else:
               # print 'z is', z
                z *= 200 / a
               # print 'z is', z
                z += z[0: 200 % a]
               # print 'z is', z
                z = Decimal('.' + z)
               # print 'z is', z
                if Decimal(str(Decimal(1)/Decimal(i))[:-1]) / z == 1:
                    decimals[i] = a
                    break
                else:
                    a += 1

{i:decimals[i] for i in decimals if decimals[i]<>0}





















