#!/usr/bin/env python3

n = int(input())
i = 1

while i <= n:
    if i % 3 == 0:
        if i % 5 == 0:
            print("fizz-buzz")
        else:
            print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
    i += 1
