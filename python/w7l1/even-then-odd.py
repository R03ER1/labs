#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(int(line))
    line = input()


i = 0
while i < len(list):
    if list[i] % 2 == 0:
        print(str(list[i]))
    i += 1
i = 0
while i < len(list):
    if list[i] % 2 == 1:
        print(str(list[i]))
    i += 1
