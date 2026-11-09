#!/usr/bin/env python3

newline = input()
maxlength = 0
lines = []
while newline != "end":
    if len(newline.split(".")[0]) > maxlength:
        maxlength = len(newline.split(".")[0])
    lines.append(newline)
    newline = input()

i = 0
while i < len(lines):
    print(" " * (maxlength - len(lines[i].split(".")[0])) + lines[i])
    i += 1
