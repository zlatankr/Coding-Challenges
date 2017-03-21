# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/pangrams
"""
a = raw_input().strip().replace(' ', '').lower()

if len(set(a)) == 26:
    print 'pangram'
else:
    print 'not pangram'