#!/usr/bin/env python3

n = int(input())
square = 0
while (square + 1) ** 2 < n:
    square += 1
print(square ** 2)
