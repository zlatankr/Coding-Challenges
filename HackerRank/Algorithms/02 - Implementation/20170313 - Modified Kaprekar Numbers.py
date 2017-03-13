# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/kaprekar-numbers

"""
p = int(raw_input().strip())
q = int(raw_input().strip())

def kaprekar(x):
    sq = x*x
    if x == 1:
        return 1
    elif len(str(sq)) > len(str(x)) and int(str(sq)[-len(str(x)):]) + int(str(sq)[:len(str(sq))-len(str(x))]) == x:
        return x
    else:
        return ''

nums = []
for i in range(p, q+1):
    if len(str(kaprekar(i))) > 0:
        nums.append(i)

if len(nums) > 0:
    for i in nums:
        print i,
else:
    print 'INVALID RANGE'