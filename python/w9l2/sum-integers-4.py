#!/usr/bin/env python3

import sys

sum = 0
lines = sys.argv[1:]
i = 0
while i < len(lines):
    with open(lines[i]) as f:
        numbers = f.read().split()
        j = 0
        while j < len(numbers):
            sum += int(numbers[j])
            j += 1
    i += 1
print(sum)
