# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/game-of-thrones
"""

string = raw_input()
 
found = True
from collections import Counter

if len(string) % 2 == 0:
    if any([Counter(string)[i] % 2 != 0 for i in Counter(string)]):
        found = False
else:
    if sum([Counter(string)[i] % 2 != 0 for i in Counter(string)]) != 1:
        found = False

if not found:
    print("NO")
else:
    print("YES")