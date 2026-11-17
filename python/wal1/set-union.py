#!/usr/bin/env python3

import sys

words = {}

with open("a.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        if line not in words:
            print(line)
            words[line] = True
        line = f.readline()
with open("b.txt") as f:
    line = f.readline()
    while line != "":
        line = line.rstrip()
        if line not in words:
            print(line)
            words[line] = True
        line = f.readline()
