#!/usr/bin/env python3

import sys

i = 1
sum = 0
while i < len(sys.argv):
    sum += int(sys.argv[i])
    i += 1
print(sum)
