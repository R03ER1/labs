#!/usr/bin/env python3

text = input()
i = 0
while text[i] > "g" or text[i] < "a":
    i += 1
print(text[i])
