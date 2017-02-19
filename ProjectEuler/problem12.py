#!/usr/bin/python

import math

# ProjectEuler.net
# Problem12
# What is the value of the first triangle number to have over five hundred divisors?

def numberOfDivisors(n):
    count = 0 #Starts at 1 to represent the number itself
    for i in range (1,int(math.floor(math.sqrt(n)))):
        if n%i == 0:
            count += 1
    return count*2
    
def calculateNthTriangleNumber(n):
    #http://en.wikipedia.org/wiki/Summation
    return n*(n+1)/2

count = 8
while 1 == 1:
    triNum = calculateNthTriangleNumber(count)
    if numberOfDivisors(triNum) > 500:
        print str(triNum)
        break
    count += 1
    
# Validated