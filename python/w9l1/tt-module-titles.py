#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    name = " ".join(newline.split()[5:])
    codes.append(name)
    newline = input()

i = 0
while i < len(codes):
    print(codes[i])
    i += 1
