#!/usr/bin/env python3

import os

dirs = ["."]
i = 0

while i < len(dirs):
    entries = os.listdir(dirs[i])
    j = 0
    while j < len(entries):
        path = dirs[i] + "/" + entries[j]
        if os.path.isdir(path):
            dirs.append(path)
        elif os.path.isfile(path):
            print(path)
        j += 1
    i += 1
