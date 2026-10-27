#!/usr/bin/env python3

list = []
line = input()

while line != "end":
    list.append(int(line))
    line = input()

n = int(input())

i = 0
while i < len(list):
    print(str(list[i] + n))
    i += 1
