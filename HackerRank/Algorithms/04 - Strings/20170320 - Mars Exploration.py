# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/mars-exploration
"""
#!/bin/python

import sys

S = raw_input().strip()
rogue = 0
for i in range(len(S)/3):
    
    if S[3*i + 1] != 'O':
        rogue += 1
        
    if S[3*i] != 'S':
        rogue += 1
        
    if S[3*i + 2] != 'S':
        rogue += 1
print rogue