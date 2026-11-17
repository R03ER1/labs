#!/usr/bin/env python3

import os

files = os.listdir(".")

i = 0
while i < len(files):
    if files[i][-4:] != ".bak" and os.path.isfile(files[i]):
        with open(files[i]) as f_in:
            with open(files[i] + ".bak", "w") as f_out:
                f_out.write(f_in.read())
    i += 1
