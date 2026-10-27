#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(line)
    line = input()

i = len(list) - 1
while i >= 0:
    print(list[i])
    i -= 1
