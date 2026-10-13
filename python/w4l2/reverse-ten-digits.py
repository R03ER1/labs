#!/usr/bin/env python3

n = 0

i = 0
while i < 10:
    n += (10 ** i) * int(input())
    i += 1

while i > 0:
    print(n // (10 ** (i - 1)))
    n = (n % (10 ** (i - 1)))
    i -= 1
