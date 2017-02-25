# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:38 2015

@author: zlatan.kremonic
"""


# 9
import timeit
"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

# first, let's find all the square numbers under 1,000:
import numpy as np
c = []
for i in range(1,100000):
    if np.sqrt(i) % 1 == 0:
        c.append(i)
print c

b = {}
for i in c:
    a = []
    for z in range(1,i+1):
        if np.sqrt(z) % 1 == 0:
            a.append(z)
    b[i] = a
print b

for i in b.keys():
    if any(np.sqrt(i) + np.sqrt(j) + (np.sqrt(i - j)) == 1000 for j in b[i]):
        print "got it" # np.sqrt(i), np.sqrt(j), (np.sqrt(i - j))

        
        
for j in a[256]:
    print j

#------------------
#------------------
"""
We know that a < b < c and that a + b + c = 1000
Therefore b < 500, and a < 350
"""

def Num_Nine():
    a = 1
    while a < 350:
        b = 1
        while b < 500:
            if 1000 - np.sqrt(np.square(a)+np.square(b)) - a - b == 0:
                print '\'a\' is ',a, '\'b\' is ',b, '\'c\' is ', np.sqrt(np.square(a)+np.square(b))
                print 'Their product is ', a*b*np.sqrt(np.square(a)+np.square(b))
                return
            b += 1
        a += 1
    return
