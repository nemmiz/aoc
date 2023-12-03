#!/usr/bin/python3

def solve(data):
    ignore = False
    depth = 0
    score = 0
    garbage = False
    removed = 0

    for c in data:
        if ignore:
            ignore = False
            continue

        if garbage:
            if c == '!':
                ignore = True
            elif c == '>':
                garbage = False
            else:
                removed += 1
        else:
            if c == '{':
                depth += 1
                score += depth
            elif c == '}':
                depth -= 1
            elif c == '<':
                garbage = True

    print(score, removed, sep='\n')


with open('../input/09.txt') as f:
    solve(f.read())
