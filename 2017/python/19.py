#!/usr/bin/python3

from string import ascii_uppercase

def solve(lines):
    x, y = lines[0].find('|'), 0
    dx, dy = 0, 1
    c = '|'
    chars = []
    steps = 0
    while c != ' ':
        x += dx
        y += dy
        c = lines[y][x]
        steps += 1
        if c in ascii_uppercase:
            chars.append(c)
        elif c == '+':
            if dx != 0:
                if lines[y-1][x] != ' ':
                    dx, dy = 0, -1
                elif lines[y+1][x] != ' ':
                    dx, dy = 0, 1
            elif dy != 0:
                if lines[y][x-1] != ' ':
                    dx, dy = -1, 0
                elif lines[y][x+1] != ' ':
                    dx, dy = 1, 0
    print(''.join(chars))
    print(steps)


with open('../input/19.txt') as f:
    lines = [line.rstrip('\n') for line in f.readlines()]
    solve(lines)
