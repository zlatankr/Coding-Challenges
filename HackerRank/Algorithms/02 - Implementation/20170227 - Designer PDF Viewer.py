# -*- coding: utf-8 -*-
"""
Link to challenge: 

https://www.hackerrank.com/challenges/designer-pdf-viewer
"""

#!/bin/python

import sys


h = map(int, raw_input().strip().split(' '))
word = raw_input().strip()

import string

print max([h[string.lowercase.index(i)] for i in word])*len(word)