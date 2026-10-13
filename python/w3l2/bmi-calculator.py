#!/usr/bin/env python3

weight = int(input())
height = int(input())

bmi = weight / (height * height) * 10000

"""
< 18.5
underweight
18.5–24.9
normal
25.0–29.9
overweight
>= 30.0
obese
"""

if bmi < 18.5:
    print("underweight")
elif bmi < 25:
    print("normal")
elif bmi < 30:
    print("overweight")
else:
    print("obese")
