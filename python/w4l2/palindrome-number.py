#!/usr/bin/env python3

text = input()
length = len(text)
n = int(text)
palindrome = True

i = 0
while i < length // 2:
    i_end = (n % 10 ** (i + 1)) // (10 ** i)
    i_start = (n // (10 ** (length - i - 1))) % 10
    if i_end != i_start:
        palindrome = False
    i += 1

if not palindrome:
    print("no")
else:
    print("yes")
