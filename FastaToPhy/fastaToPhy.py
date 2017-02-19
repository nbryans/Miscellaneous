#!/usr/bin/env python

import sys

__author__ = "Nathaniel Bryans"
__version__ = "1.0.0"

if len(sys.argv) < 2:
    print "You must include an inputfile and outfile name"
    exit()

inputfilename = sys.argv[1]
outputfilename = sys.argv[2]

fin = open(inputfilename, 'r')
fout = open(outputfilename, 'w')

speciesCount = 0
outputText = []
curLine = ""

for line in fin:
    #species lines in fasta start with a '>'
    if line[0] == '>':
        speciesCount += 1
        if curLine != "":
            outputText.append(curLine)
        curLine = line[1:].replace("\n", "") + " "*10
    else:
        curLine += line.replace("\n", "")

outputText.append(curLine)

#Find sequence length for phy file header
sequenceLength = len(outputText[0].split()[1])
#splits the first species entry using whitespace
#index 0 contains species name, index 1 contains sequence
#calculates the length of index 1

fout.write(str(speciesCount)+" ")
fout.write(str(sequenceLength)+"\n")
for i in outputText:
    fout.write(i + "\n")

fin.close()
fout.close()
