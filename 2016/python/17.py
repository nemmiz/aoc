#!/usr/bin/python3

from collections import deque
import hashlib


def directions(point, code):
    h = hashlib.md5(code.encode('ascii')).hexdigest()
    if point[1] > 0 and h[0] in 'bcdef':
        yield 'U'
    if point[1] < 3 and h[1] in 'bcdef':
        yield 'D'
    if point[0] > 0 and h[2] in 'bcdef':
        yield 'L'
    if point[0] < 3 and h[3] in 'bcdef':
        yield 'R'


def move(pos, direction):
    if direction == 'U':
        return (pos[0], pos[1]-1)
    if direction == 'D':
        return (pos[0], pos[1]+1)
    if direction == 'L':
        return (pos[0]-1, pos[1])
    if direction == 'R':
        return (pos[0]+1, pos[1])


def find_path(passcode):
    start = (0, 0)
    goal = (3, 3)
    queue = deque([(start, passcode)])

    while queue:
        pos, code = queue.popleft()
        if pos == goal:
            print(code[len(passcode):])
            return
        for d in directions(pos, code):
            queue.append((move(pos, d), code+d))


def find_longest(passcode):
    start = (0, 0)
    goal = (3, 3)
    queue = deque([(start, passcode)])
    longest = 0

    while queue:
        pos, code = queue.popleft()
        if pos == goal:
            longest = max(longest, len(code)-len(passcode))
            continue
        for d in directions(pos, code):
            queue.append((move(pos, d), code+d))
    
    print(longest)
    

find_path('dmypynyp')
find_longest('dmypynyp')
