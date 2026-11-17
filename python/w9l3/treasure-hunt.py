#!/usr/bin/env python3

import os

files = os.listdir(".")

nextfile = "start.txt"

while nextfile in files:
    with open(nextfile) as f:
        nextfile = f.read().rstrip()

print(nextfile)
