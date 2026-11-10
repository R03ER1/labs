#!/usr/bin/env python3

import sys

# incorrect!!

with open(sys.argv[1]) as file1:
    lines1 = file1.readlines()
with open(sys.argv[2]) as file2:
    lines2 = file2.readlines()

i = 0
while lines1[i] == lines2[i] and i < len(lines1) and i < len(lines2):
    i += 1

j = 0
while lines1[i][j] == lines2[i][j] and i < len(lines1[i]) and i < len(lines2[i]):
    j += 1
if i not in {len(lines2), len(lines1), len(lines2[i]), len(lines1[i])}:
    print(i, j)
