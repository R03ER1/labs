#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    codes.append(newline)
    newline = input()

day = int(input())
i = 0
while i < len(codes):
    if int(codes[i][0]) == day:
        print(codes[i])
    i += 1
