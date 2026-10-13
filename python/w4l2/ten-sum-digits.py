#!/usr/bin/env python3

i = 0
result = 0
while i < 10:
    n = int(input())
    if n < 0:
        result += -n % 10
    else:
        result += n % 10
    i += 1

print(result)
