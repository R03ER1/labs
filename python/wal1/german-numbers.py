#!/usr/bin/env python3

import sys

words = sys.stdin.readlines()

translation = {
    "one": "eins",
    "two": "zwei",
    "three": "drei",
    "four": "vier",
    "five": "funf",
    "six": "sechs",
    "seven": "sieben",
    "eight": "acht",
    "nine": "neun",
    "ten": "zehn",
}

i = 0
while i < len(words):
    print(translation[words[i].rstrip()])
    i += 1
