# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/camelcase
"""

#!/bin/python

import sys


s = raw_input().strip()

total = 1
for i in range(1, len(s)):
    total += s[i].isupper()
print total