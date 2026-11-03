#!/usr/bin/env python3

nums = []

newline = input()
while newline != "end":
    nums.append(newline)
    newline = input()

i = 0
while i < len(nums):
    j = i
    smallest = j
    while j < len(nums):
        j_years = int(nums[j][6:8]) * 360
        j_months = int(nums[j][3:5]) * 30
        j_days = int(nums[j][0:2])
        j_age = j_days + j_months + j_years
        lowest_yrs = int(nums[smallest][6:8]) * 360
        lowest_mths = int(nums[smallest][3:5]) * 30
        lowest_days = int(nums[smallest][0:2])
        lowest_age = lowest_days + lowest_mths + lowest_yrs
        if j_age < lowest_age:
            smallest = j
        #print(nums[j][9:] + " " + str(j_age))
        j += 1
    num = nums[i]
    nums[i] = nums[smallest]
    nums[smallest] = num
    print(nums[i][9:])
    i += 1
