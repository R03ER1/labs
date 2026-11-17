#!/usr/bin/env python3

import sys

fruit = {
    "apple": True,
    "pear": True,
    "orange": True,
    "banana": True,
    "cherry": True
}

words = sys.stdin.readlines()
i = 1
while i < len(words):
    if words[i].rstrip() in fruit and fruit[words[i].rstrip()]:
        sys.stdout.write(words[i])
        fruit[words[i]] = False
    i += 1
