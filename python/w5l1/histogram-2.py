#!/usr/bin/env python3

s = ""
n = int(input())
i = 0
while i < n:
    s += "*" * int(input())
    s += "\n"
    i += 1
print(s[:-1])
