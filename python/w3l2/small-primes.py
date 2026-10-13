#!/usr/bin/env python3

n = int(input())

if (n % 2 == 0 or n % 3 == 0) and (n > 3) or n == 1:
    print("not prime")
else:
    print("prime")
