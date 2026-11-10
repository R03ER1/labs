#!/usr/bin/env python3

import sys

sum = 0
line = sys.stdin.readline()
while line != "":
    sum += int(line)
    line = sys.stdin.readline()
print(sum)
