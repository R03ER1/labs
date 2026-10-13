#!/usr/bin/env python3

s = input()
modified = ""
i = 0
while i < (len(s)):
    if s[i] != " ":
        modified += s[i]
    i += 1
print(modified)
