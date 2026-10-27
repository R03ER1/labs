#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(int(line))
    line = input()

largest = list[0]
i = 0
while i < len(list):
    if list[i] > largest:
        largest = list[i]
    i += 1
print(largest)
