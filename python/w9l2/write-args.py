#!/usr/bin/env python3

import sys

with open(sys.argv[1], "w") as f:
    words = sys.argv[2:]
    i = 0
    while i < len(words):
        f.write(words[i] + "\n")
        i += 1
