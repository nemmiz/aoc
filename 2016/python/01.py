#!/usr/bin/python3

L_turn = {'N': 'W', 'S': 'E', 'W': 'S', 'E': 'N'}
R_turn = {'N': 'E', 'S': 'W', 'W': 'N', 'E': 'S'}

def part1(directions):
    x, y = 0, 0
    direction = 'N'

    for d in directions:
        if d[0] == 'L':
            direction = L_turn[direction]
        elif d[0] == 'R':
            direction = R_turn[direction]
        steps = int(d[1:])
        if direction == 'N':
            y -= steps
        elif direction == 'S':
            y += steps
        elif direction == 'W':
            x -= steps
        elif direction == 'E':
            x += steps

    print(abs(x)+abs(y))


def part2(directions):
    x, y = 0, 0
    direction = 'N'
    positions = set((x, y))

    for d in directions:
        if d[0] == 'L':
            direction = L_turn[direction]
        elif d[0] == 'R':
            direction = R_turn[direction]
        steps = int(d[1:])
        if direction == 'N':
            dx, dy = 0, -1
        elif direction == 'S':
            dx, dy = 0, 1
        elif direction == 'W':
            dx, dy = -1, 0
        elif direction == 'E':
            dx, dy = 1, 0
        for i in range(steps):
            x += dx
            y += dy
            pos = (x, y)
            if pos in positions:
                print(abs(x)+abs(y))
                return
            positions.add(pos)


with open('../input/01.txt') as f:
    dirs = f.read().replace(',', '').split()

part1(dirs)
part2(dirs)
