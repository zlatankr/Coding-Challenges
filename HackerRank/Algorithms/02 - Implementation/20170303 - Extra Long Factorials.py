# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/extra-long-factorials
"""

#!/bin/python

import sys


n = int(raw_input().strip())
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print fact(n)