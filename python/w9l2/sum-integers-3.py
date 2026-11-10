#!/usr/bin/env python3

import sys

sum = 0
lines = sys.argv[1:]
i = 0
while i < len(lines):
    with open(lines[i]) as f:
        num = f.readline()
        while num != "":
            sum += int(num)
            num = f.readline()
    i += 1
print(sum)
