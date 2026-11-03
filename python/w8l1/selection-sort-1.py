#!/usr/bin/env python3

nums = []

newline = input()
while newline != "end":
    nums.append(int(newline))
    newline = input()

smallest = 0
i = 1
while i < len(nums):
    if nums[i] < nums[smallest]:
        smallest = i
    i += 1

print(smallest)
