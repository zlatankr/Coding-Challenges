# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/save-the-prisoner
"""
cases = int(raw_input().strip())

for i in range(cases):
    N, M, S = map(int, raw_input().strip().split(' '))
    if M == 0:
        print S
    elif N >= M:
        if S - 1 + M > N:
            print (S - 1 + M) % N
        else:
            print S + (M - 1)
    elif S + ((M % N) - 1) > N:
        print (S - 1 + (M % N)) % N
    else:
        print S + ((M % N) - 1)