#!/usr/bin/python3

def do_moves(lines, start, possible_positions):
    x, y = start
    for line in lines:
        for c in line:
            if c == 'U':
                nx, ny = x, y-1
            elif c == 'D':
                nx, ny = x, y+1
            elif c == 'L':
                nx, ny = x-1, y
            elif c == 'R':
                nx, ny = x+1, y
            if (nx, ny) in possible_positions:
                x = nx
                y = ny
        print(possible_positions[(x,y)], end='')
    print()

with open('../input/02.txt') as f:
    lines = [line.strip() for line in f.readlines()]

keypad1 = {
    (0, 0): 1, (1, 0): 2, (2, 0): 3,
    (0, 1): 4, (1, 1): 5, (2, 1): 6,
    (0, 2): 7, (1, 2): 8, (2, 2): 9,
}
do_moves(lines, (1, 1), keypad1)

keypad2 = {
                          (2, 0): '1',
             (1, 1): '2', (2, 1): '3', (3, 1): '4',
(0, 2): '5', (1, 2): '6', (2, 2): '7', (3, 2): '8', (4, 2): '9',
             (1, 3): 'A', (2, 3): 'B', (3, 3): 'C',
                          (2, 4): 'D',
}
do_moves(lines, (2, 2), keypad2)
