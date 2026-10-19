#!/usr/bin/env python3

compared = int(input())
if compared != 0:
    n = int(input())
    while n != 0:
        if n > compared:
            print("higher")
        elif n < compared:
            print("lower")
        else:
            print("equal")
        compared = n
        n = int(input())
