#!/usr/bin/env python3

s = ""

i = 0
while i < 10:
    s += "*" * int(input())
    s += "\n"
    i += 1
print(s[:-1])
