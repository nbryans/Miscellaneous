#!/usr/bin/env python

from random import randint

keep = 0 # 1 means yes, 0 means no
n_iter = 1000000
n_successK = 0 #Number of success when we keep
n_successS = 0 #Number of success when we switch

for i in range(0,n_iter):
    x = [0, 0, 0]
    x[randint(0,2)] = 1
    
    # We always start pick x[0]
    
    # Remove the remaining 0 (or one of them)
    alt = -1
    if x[1] == 0:
        alt = 2
    else:
        alt = 1
        
    # Check to see if we won
    if x[0] == 1:
        n_successK += 1
    if x[alt] == 1:
        n_successS += 1
            
print "Keep Success = " + str(n_successK)
print "Switch Success = " + str(n_successS)