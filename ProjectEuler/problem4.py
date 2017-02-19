#!/usr/bin/python

import math

# ProjectEuler.net
# Problem4
# Find the largest palindrome made from the product of two 3-digit numbers. 

def isPalindrome(n):
    strN = str(n)
    lenN = len(strN)
    for i in range (0, lenN/2):
        if strN[i] != strN[lenN-1-i]:
            return 0
    return 1
    
largest = 0
for i in range (999, 99, -1):
    for j in range (999, 99, -1):
        if isPalindrome(i*j) == 1:
            if (i*j) > largest:
                largest = i*j
                
print str(largest)

# Verified Correct