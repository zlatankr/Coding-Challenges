# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/caesar-cipher-1
"""
#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())

a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_string = ''

for i in s:
    if i in a:
        if a.index(i) + 1 + k > len(a):
            new_string += a[(a.index(i) + k) % len(a)]
        else:
            new_string += a[a.index(i) + k]
    elif i in a.lower():
        if a.lower().index(i) + 1 + k > len(a):
            new_string += a[(a.lower().index(i) + k) % len(a)].lower()
        else:
            new_string += a[a.lower().index(i) + k].lower()
    else:
        new_string += i
print new_string