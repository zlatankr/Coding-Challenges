# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/separate-the-numbers
"""
#!/bin/python

import sys


q = int(raw_input().strip())
for a0 in xrange(q):
    s = raw_input().strip()
    i = 1
    j = 0
    while True:
        if len(s) == 1:
            print 'NO'
            break
        if s[j][0] == '0':
            print 'NO'
            break
        if j == 0:
            start = int(s[j:j+i])
        if int(s[j:j+i]) + 1 == int(s[j+i:j+i+i]):
            if j+i+i == len(s):
                print 'YES', start
                break
            j += i
        elif int(s[j:j+i]) + 1 == int(s[j+i:j+i+i+1]) and s[j+i] != '0':
            if j+i+i+1 == len(s):
                print 'YES', start
                break
            j += i
            i += 1
        else:
            i += 1
            j = 0
            if i > len(s)/2:
                print 'NO'
                break