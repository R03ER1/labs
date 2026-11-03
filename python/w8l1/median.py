#!/usr/bin/env python3

nums = []

newline = input()
while newline != "end":
    nums.append(int(newline))
    newline = input()

i = 0
while i < len(nums):
    j = i
    smallest = j
    while j < len(nums):
        if nums[j] < nums[smallest]:
            smallest = j
        j += 1
    num = nums[i]
    nums[i] = nums[smallest]
    nums[smallest] = num
    i += 1

print(nums[len(nums) // 2])
