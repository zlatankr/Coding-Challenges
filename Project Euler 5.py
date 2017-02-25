# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 20:00:36 2015

@author: zlatan.kremonic
"""


# 5
import timeit
"""
2520 is the smallest number that can be divided by 
each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly 
divisible by all of the numbers from 1 to 20?
"""

for i in range(1,11):
    print 2520//i

def Num_five(n, z): # n = how many dividors. z = max number
    a = 100000000
    while a < z:
        b = n
        for i in lazy_range2(n):
            if a % i <> 0:
                break
            b -= 1
            if b == 0:
                print a
                return
        a += 1
    return

# solution found online

check_list = [11, 13, 14, 16, 17, 18, 19, 20]

def find_solution(step):
    for num in xrange(step, 999999999, step):
        if all(num % n == 0 for n in check_list):
            return num
    return None

if __name__ == '__main__':
    solution = find_solution(20)
    if solution is None:
        print "No answer found"
    else:
        print "found an answer:", solution

