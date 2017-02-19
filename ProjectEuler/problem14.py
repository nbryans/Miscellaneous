#!/usr/bin/python

import math

# ProjectEuler.net
# Problem14
# Which starting number, under one million, produces the longest chain? (Using the Collatz sequence)

maxNum = 1000000

def collatzSequence(n, count, dyanmicArray):
    if n == 1:
        return count
    if n < maxNum+1 and dynamicArray[n] != 0 :
        return dynamicArray[n] + count
    if n%2 == 0:
        return collatzSequence(n/2, count+1, dyanmicArray)
    else:
        return collatzSequence(n*3+1, count+1, dynamicArray)
        
        
dynamicArray = []
for i in range (0, maxNum+1):
    dynamicArray.append(0)

longestChain = 10
intWithLongestChain = 13
for i in range(14, maxNum+1):
    x = collatzSequence(i, 1, dynamicArray)
    dynamicArray[i] = x
    if x > longestChain:
        longestChain = x
        intWithLongestChain = i
        
print str(intWithLongestChain) + " " + str(longestChain)
    
# Verified
# Added dynamic programming code. Still work but now it is much faster.