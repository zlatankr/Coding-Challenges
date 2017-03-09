# -*- coding: utf-8 -*-
"""
https://www.hackerrank.com/challenges/acm-icpc-team
"""
#!/bin/python

import sys


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
topic = []
topic_i = 0
for topic_i in xrange(n):
   topic_t = str(raw_input().strip())
   topic.append(topic_t)

def tot(i, z):
    return len(str(int(i)+int(z)).replace('0',''))
counts = [0]
for i in xrange(n-1):
    for z in xrange(i+1, n):
        if tot(topic[i], topic[z]) >= max(counts):
            counts.append(tot(topic[i], topic[z]))
print max(counts)
print len([i for i in counts if i==max(counts)])