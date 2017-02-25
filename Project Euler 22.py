# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 11:42:37 2016

Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import requests
import timeit
import string
    
def number_22():
    url = 'https://projecteuler.net/project/resources/p022_names.txt'
    
    names = requests.get(url)
    
    start = timeit.default_timer()
    names = names.content.replace("\"","")
    
    names_list = names.split(",")
    
    names_list.sort()
    
    # check if our order/content matches example from prompt
    names_list[937]
    
    scores = {}
    for i in xrange(len(string.letters[len(string.letters)/2:])):
        scores[string.letters[len(string.letters)/2:][i]] = i+1
    
    total = 0
    for order in xrange(len(names_list)):
        total += sum([scores[i] for i in names_list[order]]) * (order +1)
    
    print total
    print timeit.default_timer() - start, 'seconds'
    return