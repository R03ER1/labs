#!/usr/bin/env python3

import sys

lines = []
newline = input()
while newline != "end":
    lines.append(newline)
    newline = input()

i = 0
while i < len(lines):
    if sys.argv[1] in lines[i]:
        print(lines[i])
    i += 1
