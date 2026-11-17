#!/usr/bin/env python3

import sys

words = {}
intersection = {}
with open("a.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        words[line] = True
        line = f.readline()
with open("b.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        if line in words:
            intersection[line] = True
        line = f.readline()

if intersection == {}:
    print("disjoint")
else:
    print("intersecting")
