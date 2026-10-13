#!/usr/bin/env python3

s = input()
swapped = s[-1]

i = 1
while i < len(s) - 1:
    swapped += s[i]
    i += 1
swapped += s[0]

print(swapped)
