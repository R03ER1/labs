#!/usr/bin/env python3

"""
Mark
Classification:
>= 70
first
50–69
second
40–49
third
< 40
fail
"""

mark = int(input())

print("first:", (mark >= 70))
print("second:", 50 <= mark <= 69)
print("third:", 40 <= mark <= 49)
print("fail:", mark < 40)
