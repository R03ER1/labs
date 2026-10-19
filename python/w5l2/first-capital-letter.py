#!/usr/bin/env python3

text = input()
i = 0
while text[i] < "A" or text[i] > "Z":
    i += 1
print(i)
