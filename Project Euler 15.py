# -*- coding: utf-8 -*-
"""
Created on Thu Jan 07 14:10:29 2016

@author: zlatan.kremonic
"""
"""
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

import timeit

def doubles(n, z):
    """
    To get from one corner of the grig (0,0) to another, say (2,2), the sum 
    of each next set of coordinates always increases by 1. Thus we first want 
    to find all the combinations of coordinates that lead up to the sum of 
    our destination coordintates, such as 4 in the case of 2,2.
    This function gives us all the combinations of two numbers that 
    add up up to 'n', which is ONE of the numbers that leads to our final 
    coordinate of "z,z".
    """
    c = []
    for i in range(0, z+1):
        a = i
        b = n - i
        if b >= 0 and b < z + 1:
            c.append([a, b])
    return c

def combos(z):
    """
    This function uses our doubles function to show ALL the combinations for 
    every increasing sum of coordinates (every "LEVEL") up to 2z, our final 
    sum of coordinates.
    """
    d = {}
    for x in range(1, 2*z):
        d[x] = doubles(x,z)
    return d

def num_fifteen(p):
    j = combos(p)
    iterables = [j[values] for values in range(1,len(j)+1)]
    """
    The valid dict will let us know where each coordinate can go.
    """
    valid = {}
    for item in iterables:
        for subitem in item:
            a = []
            if subitem[0] + 1 < (p + 1):
                a.append([subitem[0] + 1, subitem[1]])
            if subitem[1] + 1 < (p + 1):
                a.append([subitem[0], subitem[1] + 1])
            valid[str(subitem)] = a
    start_t = timeit.default_timer()
    
    """
    The values dict will store how many diffeent paths led to each point.
    We start the dict with the first two points.
    """
    values = {'[0, 1]' : 1, '[1, 0]' : 1}    
    t = 1
    while t < 2*p:
        # evaluate each coordinate starting at level 1
        for item in j[t]: 
            # look at each coordinate that that point goes to
            for value in valid[str(item)]:
                # and add the values from the preceding coordinate to this next one
                if str(value) in values:
                    values[str(value)] = values[str(item)] + values[str(value)]
                else:
                    values[str(value)] = values[str(item)]
        t += 1
    print 'Runtime > ', timeit.default_timer() - start_t, ' seconds'
    print "max number of routes is ",values['['+str(p)+', '+str(p)+']']
    return

num_fifteen(20)






















