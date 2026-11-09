#!/usr/bin/env python3

newline = input()
lines = []
while newline != "end":
    lines.append(newline)
    newline = input()
alltext = " ".join(lines)
cleantext = " ".join(alltext.split())
sentences = cleantext.split(".")
i = 0
while i < len(sentences) - 1:
    print(sentences[i].strip() + ".")
    i += 1
