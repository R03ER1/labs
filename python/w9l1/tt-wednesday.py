#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    if newline[0] == "3":
        codes.append(newline)
    newline = input()

i = 0
while i < len(codes):
    print(codes[i])
    i += 1
