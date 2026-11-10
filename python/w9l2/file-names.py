#!/usr/bin/env python3

import sys

inputs = sys.stdin.readlines()
i = 0
while i < len(inputs):
    print(inputs[i].split("/")[-1].rstrip())
    i += 1
