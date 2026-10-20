#!/usr/bin/env python3

s = input()
i = 0
j = 0
k = 0
m = 0

while i < len(s) and (s[i] < "0" or s[i] > "9"):
    i += 1
if i != len(s):
    j = i
    while j < len(s) and not (s[j] < "0" or s[j] > "9"):
        j += 1

k = j + 1
while k < len(s) and (s[k] < "0" or s[k] > "9"):
    k += 1
if k != len(s):
    m = k
    while m < len(s) and not (s[m] < "0" or s[m] > "9"):
        m += 1
    print(s[k:m] + " " + str(k))
