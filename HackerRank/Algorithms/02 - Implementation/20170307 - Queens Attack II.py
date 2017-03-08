# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/queens-attack-2
"""
#!/bin/python

import sys


n,k = raw_input().strip().split(' ')
n,k = [int(n),int(k)]
rQueen,cQueen = raw_input().strip().split(' ')
y,x = [int(rQueen),int(cQueen)]
obstacles = []
for a0 in xrange(k):
    rObstacle,cObstacle = raw_input().strip().split(' ')
    obstacles.append([int(cObstacle), int(rObstacle)])
moves = 0
b1 = y - x
b2 = y + x
horright = []
horleft = []
verup = []
verdown = []
posdiagup = []
posdiagdown = []
negdiagup = []
negdiagdown = []

for i in obstacles:
    if i[0] == x and i[1] > y:
        verup.append(i[1])
    elif i[0] == x and i[1] < y:
        verdown.append(i[1])
    elif i[1] == y and i[0] > x:
        horright.append(i[0])
    elif i[1] == y and i[0] < x:
        horleft.append(i[0])
    elif i[1] - i[0] == b1 and i[0] > x:
        posdiagup.append(i[0])
    elif i[1] - i[0] == b1 and i[0] < x:
        posdiagdown.append(i[0])
    elif i[1] + i[0] == b2 and i[1] > y:
        negdiagup.append(i[1])
    elif i[1] + i[0] == b2 and i[1] < y:
        negdiagdown.append(i[1])

if len(verup) == 0:
    moves += n - y
else:
    moves += -1 + (min(verup)-y)
#print moves
if len(verdown) == 0:
    moves += y - 1
else:
    moves += -1 + (y-max(verdown))
#print moves
if len(horright) == 0:
    moves += n - x
else:
    moves += -1 + (min(horright)-x)
#print moves
if len(horleft) == 0:
    moves += x - 1
else:
    moves += -1 + (x-max(horleft))
#print moves
if len(posdiagup) == 0:
    moves += min((n - x), (n-y))
else:
    moves += -1 + (min(posdiagup)-x)
#print moves
if len(posdiagdown) == 0:
    moves += min((x - 1),(y - 1))
else:
    moves += -1 + (x-max(posdiagdown))
#print moves
if len(negdiagup) == 0:
    moves += min((x-1), (n-y))
else:
    moves += -1 + (min(negdiagup)-y)
#print moves
if len(negdiagdown) == 0:
    moves += min((n-x),(y - 1))
else:
    moves += -1 + (y-max(negdiagdown))

print moves
