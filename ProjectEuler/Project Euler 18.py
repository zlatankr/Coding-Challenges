# -*- coding: utf-8 -*-
"""
Find the maximum total from top to bottom of the triangle below:
"""

triangle ='\
75 \
95 64 \
17 47 82 \
18 35 87 10 \
20 04 82 47 65 \
19 01 23 75 03 34 \
88 02 77 73 07 63 67 \
99 65 04 28 06 16 70 92 \
41 41 26 56 83 40 80 70 33 \
41 48 72 33 47 32 37 16 94 29 \
53 71 44 65 25 43 91 52 97 51 14 \
70 11 33 28 77 73 17 78 39 68 17 57 \
91 71 52 38 17 14 91 43 58 50 27 29 48 \
63 66 04 68 89 53 67 30 73 16 69 87 40 31 \
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'

import timeit


# Let's see how many total paths there are:
        
z = 1
a = 0
while a < 14:
    z = z*2
    print 'for', a+2, 'rows in a triangle, there are', z, 'combinations.'
    a += 1


# Turn the triangle into a dictionary, where keys are depth of triangle:
    
triangle = triangle.split()

triangle = [int(i) for i in triangle]

tree = {}
x = 0
for i in xrange(15):
    tree[i] = triangle[x: x + i + 1]
    x += i+1

# Our answer - note, this is the brue force answer...

def number_18(n):
    start_t = timeit.default_timer()
    # our dict starts with the index of the first row of the triangle and the its value
    combos = {'0': 75}
    # starting with the second row of the triangle
    for i in range(1, n):
#        print 'i is', i
        # we look at each key in our combos dectionary (each key is a possible path)
        for x in combos.keys():
#            print 'x is', x
            # and look at the index of each number in the the row of the triangle
            for z in xrange(len(tree[i])):
#                print 'z is', z
#                print 'value is', tree[i][z]
                # if that index is equal to or just one greater than the last number in the key
                # then we create a new key (valid path) whose value is the new sum of that path
                if str(z) == x.split()[-1]:
                    combos[x+' '+str(z)] = combos[x] + tree[i][z]
#                    print 'new combos is', combos
                if str(z - 1) == x.split()[-1]:
                    combos[x+' '+str(z)] = combos[x] + tree[i][z]
#                    print 'new combos is', combos
#            print 'deleting x', x
#            print 'deleting combos',combos[x]
            # then we delete the key that we just evaluated in the dictionary
            del(combos[x])
#            print 'new combos is', combos  
    print combos
    print len(combos)
    print 'Runtime > ', timeit.default_timer() - start_t, ' seconds'
    return max(combos.values())
    