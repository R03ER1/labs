#!/usr/bin/env python3

lines = []
newline = input()
while newline != "end":
    i = 0
    duplicate = 0
    while i < len(lines):
        if lines[i] == newline:
            duplicate = 1
        i += 1
    if not duplicate:
        lines.append(newline)
    newline = input()
i = 0
while i < len(lines):
    print(lines[i])
    i += 1
