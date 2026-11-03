#!/usr/bin/env python3

frequency = []
i = 0
while i < 10:
    frequency.append(0)
    i += 1

newline = input()
while newline != "end":
    frequency[int(newline)] += 1
    newline = input()

i = 0
while i < 10:
    print(str(i) + " " + "*" * frequency[i])
    i += 1
