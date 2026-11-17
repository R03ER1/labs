#!/usr/bin/env python3

import sys

attempts = sys.stdin.readlines()

tasks = {}

i = 0
while i < len(attempts):
    words = attempts[i].rstrip().split(".")
    if words[-1] == "incorrect":
        tasks[attempts[i][:-11]] = False
    if words[-1] == "correct":
        tasks[attempts[i][:-9]] = True
    i += 1

for task, value in tasks.items():
    if value:
        print(task)
