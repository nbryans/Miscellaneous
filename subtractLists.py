#!/usr/bin/env python

"""
Short demo on subtracting lists in python
"""

list1 = []
list2 = []
list3 = []
list4 = []

f = open("ListMain.txt", "r")
for line in f:
    list1.append(line.rstrip())

f = open("ListSub1.txt", "r")
for line in f:
    list2.append(line.rstrip())

f = open("ListSub2.txt", "r")
for line in f:
    list3.append(line.rstrip())

f = open("ListSub3.txt", "r")
for line in f:
    list4.append(line.rstrip())


x = [item for item in list1 if item not in list2]
y = [item for item in x if item not in list3]
z = [item for item in y if item not in list4]
#z = [item for item in [item1 for item1 in list1 if item1 not in list2] if item not in list3]


print z
#Z is equivalent of running x and y