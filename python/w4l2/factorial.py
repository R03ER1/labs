#!/usr/bin/env python3

n = int(input())
i = n
result = 1

while i > 0:
    result *= i
    i -= 1

print(result)
