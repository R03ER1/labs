#!/usr/bin/env python3

n = 0
i = 0

while i < 10:
    val = int(input())
    if val < 0:
        n += val * -1
    else:
        n += val
    i += 1

print(n)
