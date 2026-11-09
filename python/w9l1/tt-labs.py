#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    if int(newline.split()[2]) > 1:
        codes.append(newline)
    newline = input()

i = 0
while i < len(codes):
    print(codes[i])
    i += 1
