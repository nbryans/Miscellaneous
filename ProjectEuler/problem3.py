#!/usr/bin/python

import math

# ProjectEuler.net
# Problem3
# What is the largest prime factor of the number 600851475143 

# Help from stackoverflow.com/questions/23287/largest-prime-factor-of-a-number 
# Users Triptych and nhahtdh

num = 600851475143

factors = []

d = 2

while num > 1:
    while num%d == 0:
        factors.append(d)
        num /= d
    d = d+1
    
print factors

# Verified Correct (though I wouldn't say I solved this one on my own)