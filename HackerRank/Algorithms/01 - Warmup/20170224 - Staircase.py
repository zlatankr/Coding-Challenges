# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 15:09:58 2017

@author: User
"""

#!/bin/python

import sys


n = int(raw_input().strip())

for i in range(1, n+1):
    print (n-i)*' '+i*'#'