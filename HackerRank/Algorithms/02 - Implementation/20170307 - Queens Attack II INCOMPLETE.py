# -*- coding: utf-8 -*-
"""
Created on Tue Mar 07 10:38:36 2017

@author: User
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
up = 1
while up == 1:
    if [x, y+1] in obstacles:
        up = 0
    elif y + 1 < n+1:
        moves += 1
        y += 1
    else:
        up = 0
y,x = [int(rQueen),int(cQueen)]
down = 1

while down == 1:
    if [x, y-1] in obstacles:
        down = 0
    elif y - 1 > 0:
        moves += 1
        y -= 1
    else:
        down = 0
y,x = [int(rQueen),int(cQueen)]
left = 1

while left == 1:
    if [x-1, y] in obstacles:
        left = 0
    elif x - 1 > 0:
        moves += 1
        x -= 1
    else:
        left = 0
y,x = [int(rQueen),int(cQueen)]
right = 1

while right == 1:
    if [x+1, y] in obstacles:
        right = 0
    elif x + 1 < n+1:
        moves += 1
        x += 1
    else:
        right = 0
y,x = [int(rQueen),int(cQueen)]
upright = 1

while upright == 1:
    if [x+1, y+1] in obstacles:
        upright = 0
    elif x + 1 < n+1 and y + 1 < n+1:
        moves += 1
        x += 1
        y += 1
    else:
        upright = 0
y,x = [int(rQueen),int(cQueen)]
downright = 1

while downright == 1:
    if [x+1, y-1] in obstacles:
        downright = 0
    elif x + 1 < n+1 and y - 1 > 0:
        moves += 1
        x += 1
        y -= 1
    else:
        downright = 0
y,x = [int(rQueen),int(cQueen)]
upleft = 1

while upleft == 1:
    if [x-1, y+1] in obstacles:
        upleft = 0
    elif x - 1 > 0 and y + 1 < n+1:
        moves += 1
        x -= 1
        y += 1
    else:
        upleft = 0
y,x = [int(rQueen),int(cQueen)]
downleft = 1

while downleft == 1:
    if [x-1, y-1] in obstacles:
        downleft = 0
    elif x - 1 > 0 and y - 1 > 0:
        moves += 1
        x -= 1
        y -= 1
    else:
        downleft = 0
print moves