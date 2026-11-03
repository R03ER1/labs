#!/usr/bin/env python3

nums = []

newline = input()
while newline != "end":
    nums.append(int(newline))
    newline = input()

start = int(input())
smallest = start
i = start
while i < len(nums):
    if nums[i] < nums[smallest]:
        smallest = i
    i += 1

print(smallest)
