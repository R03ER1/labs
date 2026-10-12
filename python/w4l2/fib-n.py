#!/usr/bin/env python3

n = int(input())
i = 0

a = 0
b = 1

while i < n:
    if i == 0:
        print(a)
    elif i == 1:
        print(b)
    else:
        print(a + b)
        b = a + b
        a = b - a
    i += 1
