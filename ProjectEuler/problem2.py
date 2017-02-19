#!/usr/bin/python

# ProjectEuler.net
# Problem2
# Find the sum of the even fibonnaci numbers below 4 million

maxNum = 4000000

num1 = 1
num2 = 2
sum = 2

while (num1+num2) < maxNum:
        nextNum = num1 + num2
        if nextNum%2 == 0:
            sum += nextNum
        num1 = num2
        num2 = nextNum
         
print str(sum)

# Verified Correct

