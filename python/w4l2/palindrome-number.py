#!/usr/bin/env python3

text = input()
length = len(text)
n = int(text)
palindrome = True

i = 0
while i < length // 2:
    if (n % (10 ** i + 1)) // (10 ** (i)) != ((n // (10 ** (length - i))) % 10):
        palindrome == False

if not palindrome:
    print("no")
else:
    print("yes")
