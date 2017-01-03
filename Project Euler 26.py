# -*- coding: utf-8 -*-
"""
Created on Mon Jan 02 12:01:08 9017

A unit fraction contains 1 in the numerator. 
The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. 
It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle 
in its decimal fraction part.

"""

"""
- Create an empty dict

- for each n in 2 to 1000:

- if n is in dict, skip to next one
    
- if 1000 is perfectly divisible by n
    - add n and 1000/n to dict with value: 0

- if number of decimals is less than 100:
    - add n to dict with value: 0
    
- Else create a function with a while loop up to 100:
    - takes one decimal at a time (equal to wherever the while loop is)
    - repeats it until we have 100 of those number
    - divides our orinal number by the new number
    - if we get a one, then that's how many repeating numbers there
    - add n to dict with vale equal to value of while loop

"""
# note: this is a horrible solution in so many ways, but it yielded the right 
# answer so I'm moving on, for better or for worse. Electing to go for quantity
# over quality


from decimal import *

getcontext().prec = 1905
decimals = {}

for i in xrange(2, 1000):
   # print 'i is', i
    if i in decimals:
        pass
    elif float(1000) % i == 0:
        decimals[i] = 0
        decimals[int(float(1000)/i)] = 0
    elif len(str(Decimal(1)/Decimal(i))) > 1900:
        a = 1
        while a < 1900:
            #print 'a is', a
            z = str(Decimal(1)/Decimal(i))[2:(2+a)]
            if int(z) == 0:
                a += 1
            else:
               # print 'z is', z
                z *= 1900 / a
               # print 'z is', z
                z += z[0: 1900 % a]
               # print 'z is', z
                z = Decimal('.' + z)
                #print 'z is', z
                if str((Decimal(1)/Decimal(i)))[0:len(str(Decimal(z)))] == str(Decimal(z)):
                    decimals[i] = a
                    break
                else:
                    a += 1
        if a == 1900:
            a = 1
            while a < 1900:
                #print 'a2 is', a
                x = str(Decimal(1)/Decimal(i))[2]
                z = str(Decimal(1)/Decimal(i))[3:(3+a)]
                if int(z) == 0:
                    a += 1
                else:
                   # print 'z is', z
                    z *= 1900 / a
                   # print 'z is', z
                    z += z[0: 1900 % a]
                   # print 'z is', z
                    z = Decimal('.' + x + z)
                    #print 'new z is', z
                    #print 'len z', len(str(z))
                    #print 'dividing', str(Decimal(1)/Decimal(i))
                    #print 'len is', len(str(Decimal(1)/Decimal(i)))
                    if str((Decimal(1)/Decimal(i)))[0:len(str(Decimal(z)))] == str(Decimal(z)):
                        decimals[i] = a
                        break
                    else:
                        a += 1
        if a == 1900:
            a = 1
            while a < 1900:
                #print 'a3 is', a
                x = str(Decimal(1)/Decimal(i))[2:4]
                z = str(Decimal(1)/Decimal(i))[4:(4+a)]
                if int(z) == 0:
                    a += 1
                else:
                   # print 'z is', z
                    z *= 1900 / a
                   # print 'z is', z
                    z += z[0: 1900 % a]
                   # print 'z is', z
                    z = Decimal('.' + x + z)
                    #print 'new2 z is', z
                    #print 'len z', len(str(z))
                    #print 'dividing', str(Decimal(1)/Decimal(i))
                    #print 'len is', len(str(Decimal(1)/Decimal(i)))
                    if str((Decimal(1)/Decimal(i)))[0:len(str(Decimal(z)))] == str(Decimal(z)):
                        decimals[i] = a
                        break
                    else:
                        a += 1
        if a == 1900:
            a = 1
            while a < 1900:
                #print 'a4 is', a
                x = str(Decimal(1)/Decimal(i))[2:5]
                z = str(Decimal(1)/Decimal(i))[5:(5+a)]
                if int(z) == 0:
                    a += 1
                else:
                   # print 'z is', z
                    z *= 1900 / a
                   # print 'z is', z
                    z += z[0: 1900 % a]
                   # print 'z is', z
                    z = Decimal('.' + x + z)
                    #print 'new3 z is', z
                    #print 'len z', len(str(z))
                    #print 'dividing', str(Decimal(1)/Decimal(i))
                    #print 'len is', len(str(Decimal(1)/Decimal(i)))
                    if str((Decimal(1)/Decimal(i)))[0:len(str(Decimal(z)))] == str(Decimal(z)):
                        decimals[i] = a
                        break
                    else:
                        a += 1           

nonz = {i:decimals[i] for i in decimals if (decimals[i]<>0) and (decimals[i]<>1899)}

max(nonz, key=nonz.get)






