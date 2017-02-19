#!/usr/bin/python

import math

# Nathaniel Bryans
# ProjectEuler.net
# Problem16
# What is the sum of the digits of the number 2^1000

#x = math.pow(2, 1000)
x = 2**1000
y = str(int(x))

count = 0

for i in y:
    count = count + int(i)
    
print str(count)

# Validated