#!/usr/bin/env python3

newline = input()
maxlength = 0
lines = []
while newline != "end":
    if len(newline) > maxlength:
        maxlength = len(newline)
    lines.append(newline)
    newline = input()

i = 0
while i < len(lines):
    print(" " * (maxlength - len(lines[i])) + lines[i])
    i += 1
