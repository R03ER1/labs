#!/usr/bin/env python3

n = int(input())
i = 0
result = int(input())

while i < n:
    print(result)
    if result % 2 == 0:
        result //= 2
    else:
        result = result * 3 + 1
    i += 1
