#!/usr/bin/env python3

newline = input()
codes = 0
while newline != "end":
    tokens = newline.split()
    codes += int(tokens[2])
    newline = input()

print(codes)
