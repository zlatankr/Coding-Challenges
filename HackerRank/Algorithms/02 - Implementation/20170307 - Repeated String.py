# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/repeated-string
"""
#!/bin/python

import sys


s = raw_input().strip()
n = long(raw_input().strip())

print (n/len(s))*sum([1 for i in s if i=='a']) + sum([1 for i in s[:(n%(len(s)))] if i=='a'])