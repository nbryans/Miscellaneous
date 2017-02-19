#!/usr/bin/env python

"""
Implementation of Bubblesort
Adapted from Introduction to Algorithms, by Cormen et al.
"""

__author__ = "Nathaniel Bryans"

#BUBBLESORT(A)
#for i = 1 to A.length-1
#    for j = A.length downto i + 1
#        if A[j] < A[j-1]
#            exchange A[j] with A[j-1]

def Bubblesort(A):
    for i in range(len(A)):
        for j in range(len(A)-1, i, -1): # *Note the -1 (giving direction of range)
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1] # *Note the use of simultaneous assignment, avoiding the tmp