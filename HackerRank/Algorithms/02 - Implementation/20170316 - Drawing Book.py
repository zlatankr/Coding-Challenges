# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/drawing-book
"""

#!/bin/python

import sys


n = int(raw_input().strip())
p = int(raw_input().strip())

print min(p/2, (n-p)/2)
