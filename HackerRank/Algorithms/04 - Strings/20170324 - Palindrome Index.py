# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/palindrome-index
"""

def palindrome(s):
    if s[0:len(s)/2] == s[::-1][0:len(s)/2]:
        return True
    else:
        return False

n = int(raw_input().strip())

for x in range(n):
    s = raw_input().strip()
    a = list(s)
    if palindrome(s) == True:
        print -1
    else:
        for i in range(len(s)/2):
            if s[i] == s[::-1][i]:
                pass
            elif palindrome(s[i+1:len(s)-i]) == True:
                print i
                break
            elif palindrome(s[i:len(s)-i-1]) == True:
                print len(s)-i-1
                break
            elif i == len(s)/2 - 1:
                print -1