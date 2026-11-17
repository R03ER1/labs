#!/usr/bin/env python3

import sys

words = {}

with open("b.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        words[line] = True
        line = f.readline()
with open("a.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        if line not in words:
            print(line)
        line = f.readline()
