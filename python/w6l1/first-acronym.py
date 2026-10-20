#!/usr/bin/env python3

s = input()
i = 0

while i < len(s) and (s[i] < "A" or s[i] > "Z"):
    i += 1
if i != len(s):
    j = i
    while j < len(s) and not (s[j] < "A" or s[j] > "Z"):
        j += 1
    print(s[i:j] + " " + str(i))
