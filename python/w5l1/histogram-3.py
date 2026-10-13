#!/usr/bin/env python3

s = input()
result = ""
i = 0
while i < len(s):
    n = int(s[i])
    result += "*" * n
    result += "\n"
    i += 1
print(result[:-1])
