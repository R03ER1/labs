#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

translation = {}

with open("translation.txt") as f:
    line = f.readline()
    while line != "":
        translation[line.split()[0]] = line.split()[1]
        line = f.readline()

i = 0
while i < len(words):
    print(translation[words[i].rstrip()])
    i += 1
