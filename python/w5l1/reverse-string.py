#!/usr/bin/env python3

s = input()
i = len(s) - 1
reversed = ""
while i >= 0:
    reversed += s[i]
    i -= 1
print(reversed)
