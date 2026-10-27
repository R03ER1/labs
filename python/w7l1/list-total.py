#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(int(line))
    line = input()

sum = 0
i = 0
while i < len(list):
    sum += list[i]
    i += 1
print(sum)
