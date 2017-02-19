#!/usr/bin/env python

"""
Implementation of Quicksort
Adapted from Introduction to Algorithms, by Cormen et al.
>from SortingNB import Quicksort
>Quicksort.Quicksort(A)
"""

__author__ = "Nathaniel Bryans"

#QUICKSORT(A,p,r)
#if p < r
#    q = PARTITION(A,p,r)
#    QUICKSORT(A,p,q-1)
#    QUICKSORT(A,q+1,r)

#PARTITION(A,p,r)
#x = A[r]                    # x is our pivot
#i = p-1
#for j = p to r-1
#    if A[j] <= x
#        i = i + 1
#        echange A[i] with A[j]
#exchange A[i+1] with A[r]   # Put the pivot in it's place
#return i + 1

def Partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i + 1

def Quicksort(A, p=0, r=None):
    if r is None:
        r = len(A)-1
    if p < r:
        q = Partition(A, p, r)
        Quicksort(A, p,q-1)
        Quicksort(A, q+1,r)