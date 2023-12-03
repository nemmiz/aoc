#!/usr/bin/python3

def turn_left(dx, dy):
    if dx == 0:
        return (-1, 0) if dy == -1 else (1, 0)
    return (0, 1) if dx == -1 else (0, -1)

def turn_right(dx, dy):
    if dx == 0:
        return (1, 0) if dy == -1 else (-1, 0)
    return (0, -1) if dx == -1 else (0, 1)

def part1(infected_nodes, cx, cy, dx, dy):
    nodes = infected_nodes.copy()
    infections = 0
    for steps in range(10000):
        pos = (cx, cy)
        if pos in nodes:
            dx, dy = turn_right(dx, dy)
            nodes.remove(pos)
        else:
            dx, dy = turn_left(dx, dy)
            nodes.add(pos)
            infections += 1
        cx += dx
        cy += dy
    print(infections)

def part2(infected_nodes, cx, cy, dx, dy):
    nodes = {node: '#' for node in infected_nodes}
    infections = 0
    for steps in range(10000000):
        pos = (cx, cy)
        state = nodes.get(pos)
        if state is None:
            dx, dy = turn_left(dx, dy)
            nodes[pos] = 'W'
        elif state == 'W':
            nodes[pos] = '#'
            infections += 1
        elif state == '#':
            dx, dy = turn_right(dx, dy)
            nodes[pos] = 'F'
        elif state == 'F':
            dx, dy = -dx, -dy
            del nodes[pos]
        cx += dx
        cy += dy
    print(infections)

with open('../input/22.txt') as f:
    infected_nodes = set()
    for y, line in enumerate(f.readlines()):
        for x, c in enumerate(line.strip()):
            if c == '#':
                infected_nodes.add((x, y))
    carrier_x = x//2
    carrier_y = y//2

part1(infected_nodes, carrier_x, carrier_y, 0, -1)
part2(infected_nodes, carrier_x, carrier_y, 0, -1)
