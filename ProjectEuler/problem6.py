#!/usr/bin/python

import math

# ProjectEuler.net
# Problem6
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sumOfSquare = 0
squareOfSum = 0

for i in range(1, 101):
    sumOfSquare += math.pow(i,2)
    squareOfSum += i
    
squareOfSum = math.pow(squareOfSum, 2)

print str(squareOfSum - sumOfSquare)

# Verified Correct

