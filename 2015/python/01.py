#!/usr/bin/python3

with open('../input/01.txt') as f:
    floor = 0
    first_enters_basement = None
    for i, c in enumerate(f.read()):
        if c == '(':
            floor += 1
        elif c == ')':
            floor -= 1
        if floor == -1 and first_enters_basement is None:
            first_enters_basement = i + 1
    print(floor)
    print(first_enters_basement)