# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/beautiful-binary-string
"""

#!/bin/python

import sys


n = int(raw_input().strip())
B = raw_input().strip()
B = list(B)

tots = 0
for i in range(2, len(B)):
    if B[i-2:i+1] == list('010'):
        B[i] = '1'
        tots += 1
print tots