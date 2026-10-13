#!/usr/bin/env python3

n = int(input())
i = 0
result = 0
while i < n:
    print(result)
    result = result + ((result % 2) * -2)
    result += 1
    result *= -1
    i += 1
