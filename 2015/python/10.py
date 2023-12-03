#!/usr/bin/python3

from itertools import groupby

def look_and_say(sequence):
    out = []
    for x, it in groupby(sequence):
        out.append(len(list(it)))
        out.append(x)
    return out

value = [int(c) for c in '1321131112']
for i in range(50):
    value = look_and_say(value)
    if i == 39 or i == 49:
        print(len(value))