# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/grading
"""

#!/bin/python

import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    if grade > 35 and grade % 5 >= 3:
        print grade + (5- (grade % 5))
    else:
        print grade