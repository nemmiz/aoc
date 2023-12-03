#!/usr/bin/python3

from collections import deque


def simulate(commands, overrides=None):
    queue = deque(commands)
    wires = {}

    while queue:
        item = queue.popleft()

        if overrides:
            wires.update(overrides)

        try:
            if len(item) == 3:
                a = int(item[0]) if item[0].isdecimal() else wires[item[0]]
                wires[item[2]] = a
            if len(item) == 4:
                a = int(item[1]) if item[1].isdecimal() else wires[item[1]]
                wires[item[3]] = ~a & 0xFFFF
            if len(item) == 5:
                a = int(item[0]) if item[0].isdecimal() else wires[item[0]]
                b = int(item[2]) if item[2].isdecimal() else wires[item[2]]
                if item[1] == 'OR':
                    wires[item[4]] = a | b
                elif item[1] == 'AND':
                    wires[item[4]] = a & b
                elif item[1] == 'LSHIFT':
                    wires[item[4]] = (a << b) & 0xFFFF
                elif item[1] == 'RSHIFT':
                    wires[item[4]] = (a >> b) & 0xFFFF
        except KeyError:
            queue.append(item)
        
    return wires['a']


with open('../input/07.txt') as f:
    commands = [line.split() for line in f.readlines()]

part1_result = simulate(commands)
part2_result = simulate(commands, overrides={'b': part1_result})

print(part1_result)
print(part2_result)
