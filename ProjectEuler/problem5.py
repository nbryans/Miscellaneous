#!/usr/bin/python

import math

# ProjectEuler.net
# Problem5
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Try Brute Force Approach
def divisibleByAllUpToTwenty(num):
    for i in range(3,21):
        if num%i != 0:
            return 0
    return 1

done = 0
count = 20;
while done == 0:
    if divisibleByAllUpToTwenty(count) == 1:
        print str(count)
        break
    count += 2
    
# Verified Correct
# Current approach takes over a minute on i5