#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

seen = {}

snap = ""

i = 0
while i < len(words) and snap == "":
    if words[i] not in seen:
        seen[words[i]] = False
    else:
        seen[words[i]] = True
        snap = words[i]
        print("snap: " + words[i].rstrip())
    i += 1
