#!/usr/bin/env python3

with open("irish-dobs.txt") as f_in:
    with open("american-dobs.txt", "w") as f_out:
        newline = f_in.readline()
        while newline != "":
            dob = ""
            dob += newline.split("/")[1]
            dob += "/"
            dob += newline.split("/")[0]
            dob += "/"
            dob += newline.split("/")[2]
            f_out.write(dob)
            newline = f_in.readline()
