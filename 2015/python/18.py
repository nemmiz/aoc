#!/usr/bin/python3

from copy import deepcopy

def neighbors(x, y):
    yield (x-1, y-1)
    yield (x, y-1)
    yield (x+1, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x-1, y+1)
    yield (x, y+1)
    yield (x+1, y+1)

def next_state(state, always_on=[]):
    rows = len(state)
    cols = len(state[0])
    new_state = []

    for x, y in always_on:
        state[y][x] = '#'

    for y, row in enumerate(state):
        new_row = []
        for x, c in enumerate(row):
            n = 0
            for nx, ny in neighbors(x, y):
                if nx >= 0 and ny >= 0 and nx < cols and ny < rows and state[ny][nx] == '#':
                    n += 1
            if c == '#' and n in [2,3]:
                new_row.append('#')
            elif c == '.' and n == 3:
                new_row.append('#')
            else:
                new_row.append('.')
        new_state.append(new_row)

    for x, y in always_on:
        new_state[y][x] = '#'

    return new_state

def print_state(state):
    for row in state:
        print(''.join(row))

def count_lights(state):
    n = 0
    for row in state:
        n += row.count('#')
    return n

with open('../input/18.txt') as f:
    initial_state = [list(line.strip()) for line in f.readlines()]

state = deepcopy(initial_state)
for i in range(100):
    state = next_state(state)
print(count_lights(state))

state = deepcopy(initial_state)
for i in range(100):
    state = next_state(state, always_on=[(0,0),(0,-1),(-1,0),(-1,-1)])
print(count_lights(state))
