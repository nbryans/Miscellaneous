#!/usr/bin/python

import math

# ProjectEuler.net
# Problem9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc

def isPythogorean(a, b, c):
    if (math.pow(a,2)+math.pow(b,2)) == math.pow(c,2):
        return 1
        
    return 0
    
k = 1
for i in range (1, 1000):
    for j in range (i, 1000):
        k  = 1000 - i - j
        if k > i and k > j:
            if isPythogorean(i,j,k) == 1:
                print str(i) + " " + str(j) + " " + str(k)
                print str(i*j*k)
        