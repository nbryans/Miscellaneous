﻿#!/usr/bin/python

import math

# ProjectEuler.net
# Problem8
# Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?

def productOfRange(str):
    product = 1
    for i in range(0, len(str)):
        product *= int(str[i])
        
    return product

largeNum =    "73167176531330624919225119674426574742355349194934"
largeNum +=  "96983520312774506326239578318016984801869478851843"
largeNum +=  "85861560789112949495459501737958331952853208805511"
largeNum +=  "12540698747158523863050715693290963295227443043557"
largeNum +=  "66896648950445244523161731856403098711121722383113"
largeNum +=  "62229893423380308135336276614282806444486645238749"
largeNum +=  "30358907296290491560440772390713810515859307960866"
largeNum +=  "70172427121883998797908792274921901699720888093776"
largeNum +=  "65727333001053367881220235421809751254540594752243"
largeNum +=  "52584907711670556013604839586446706324415722155397"
largeNum +=  "53697817977846174064955149290862569321978468622482"
largeNum +=  "83972241375657056057490261407972968652414535100474"
largeNum +=  "82166370484403199890008895243450658541227588666881"
largeNum +=  "16427171479924442928230863465674813919123162824586"
largeNum +=  "17866458359124566529476545682848912883142607690042"
largeNum +=  "24219022671055626321111109370544217506941658960408"
largeNum +=  "07198403850962455444362981230987879927244284909188"
largeNum +=  "84580156166097919133875499200524063689912560717606"
largeNum +=  "05886116467109405077541002256983155200055935729725"
largeNum +=  "71636269561882670428252483600823257530420752963450"
    

largestProd = 0;
nums = ""    
for i in range (0, len(largeNum)-13):
    substr = largeNum[i:i+13]
    if not "0" in substr:   # This check is an optimization
        prod = productOfRange(substr)
        if prod > largestProd:
            largestProd = prod
            nums = substr
        
print str(largestProd)
print nums

# Verified Correct
