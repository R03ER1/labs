#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(line)
    line = input()

i = 0
while i < len(list):
    print(str(i) + " " + str(len(list)) + " " + list[i])
    i += 1
