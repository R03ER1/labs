#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    tokens = newline.split()
    codes.append(tokens[3])
    newline = input()

i = 0
while i < len(codes):
    print(codes[i])
    i += 1
