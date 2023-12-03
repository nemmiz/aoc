#!/usr/bin/python3


def can_reach_0(n, connections, visited):
    if n in visited:
        return False
    visited.add(n)
    if n == 0:
        return True
    if 0 in connections[n]:
        return True
    for n2 in connections[n]:
        if can_reach_0(n2, connections, visited):
            return True
    return False
    

def part1(connections):
    total = 0
    for conn in connections:
        visited = set()
        if can_reach_0(conn, connections, visited):
            total += 1
    print(total)


def part2(connections):
    sets = []
    for conn in connections:
        s = set()
        s.add(conn)
        s.update(connections[conn])
        sets.append(s)
    total = 0
    while sets:
        s = sets.pop()
        while True:
            for i in range(len(sets)):
                if not s.isdisjoint(sets[i]):
                    s.update(sets[i])
                    del sets[i]
                    break
            else:
                break
        total += 1
    print(total)


with open('../input/12.txt') as f:
    connections = {}
    for line in f.readlines():
        parts = line.replace(',', '').split()
        connections[int(parts[0])] = [int(x) for x in parts[2:]]

part1(connections)
part2(connections)
