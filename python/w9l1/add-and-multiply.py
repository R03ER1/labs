#!/usr/bin/env python3

expression = input()

split_by_plus = expression.split("+")
result = 0
i = 0
while i < len(split_by_plus):
    split_by_star = split_by_plus[i].split("*")
    j = 0
    addition = 1
    while j < len(split_by_star):
        addition *= int(split_by_star[j])
        j += 1
    result += addition
    i += 1

print(result)
