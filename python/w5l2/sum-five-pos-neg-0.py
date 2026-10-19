#!/usr/bin/env python3

positive = 0
negative = 0
n = int(input())
while n != 0:
    if n < 0:
        negative += n
    else:
        positive += n
    n = int(input())
print(str(negative) + " " + str(positive))
