#!/usr/bin/env python3

newline = input()
codes = []
while newline != "end":
    words = newline.split()
    starting_hour = int(words[1])
    length = int(words[2])
    words[1] = str(starting_hour) + ":00"
    words[2] = str(starting_hour + length - 1) + ":50"
    codes.append(" ".join(words))
    newline = input()

i = 0
while i < len(codes):
    print(codes[i])
    i += 1
