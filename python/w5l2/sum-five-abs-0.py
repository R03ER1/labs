#!/usr/bin/env python3

sum = 0
n = int(input())
while n != 0:
    if n < 0:
        sum += -1 * n
    else:
        sum += n
    n = int(input())
print(sum)
