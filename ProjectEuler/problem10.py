#!/usr/bin/python

import math

# ProjectEuler.net
# Problem10
# Find the sum of all the primes below two million. 

maxNum = 2000000
primes = [2, 3, 5, 7, 11]

def isPrime(num):
    maxCheck = math.sqrt(num)

    for i in primes:
        if i > maxCheck: # This is an optimization
            break
        if num%i == 0:
            return 0
    return 1

for i in range(13, maxNum, 2):
    if isPrime(i) == 1:
        primes.append(i)
        
sum = 0

for i in primes:
    sum += i
    
print str(sum)

# Verified