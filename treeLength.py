#!/usr/bin/env python

"""
Calculates the length of a give tree file
Date: Feb, 25 2016
"""

import sys
import re

__author__ = "Nathaniel Bryans"
__version__ = "1.0.0"

if len(sys.argv) < 1:
    print "You must include an inputfile name"
    exit()

inputfilename = sys.argv[1]

fin = open(inputfilename, 'r')

tree = fin.readline()

branchLengths = re.findall('\d+\.\d+', tree)
#print branchLengths

totalLength = 0

for i in branchLengths:
	totalLength += float(i)

print "The total length of the tree is: " + str(totalLength)