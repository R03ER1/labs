#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    with open(files[i]) as f:
        firstline = f.readline()
        empty = firstline == ""
        pyFile = files[i][-3:] == ".py"
        shabang = firstline == "#!/usr/bin/env python3\n"
        if shabang or (pyFile and not empty):
            print(files[i])
    i += 1
