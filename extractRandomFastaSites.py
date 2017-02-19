#!/usr/bin/python
import random

N = 1000 #Number of sites to randomly generate
maxIndex = 7594374 #The length of the sequences in the fasta file

fout = open("subSequence.fa", "w")
fin = open("input/seq.fa", "r")

randomNums = random.sample(range(1, maxIndex), N)
randomNums.sort()

curSequence = ""
subSequence = ""
start = 0

for line in fin:
    if line[0] == '>':
        if start != 0:
            for i in randomNums:
                subSequence += curSequence[i-1]
            fout.write(subSequence + '\n')
            curSequence = ""
            subSequence = ""
        else:
            start = 1
        fout.write(line)
    else:
        curSequence += line.rstrip()

#This clears the final line (since there isn't a final '>')
for i in randomNums:
    subSequence += curSequence[i-1]
fout.write(subSequence)

fSiteList = open("ranSiteList.txt", "w")
for i in randomNums:
    fSiteList.write(str(i) + '\n')
fout.close()
fin.close()
fSiteList.close()
