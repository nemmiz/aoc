#!/usr/bin/python3

def remaining(parts, part_to_remove):
    p = parts[:]
    p.remove(part_to_remove)
    return p

def strength(bridge):
    return sum((a+b for a, b in bridge))

def build(bridge, parts, required, bridges):
    for p in parts:
        if p[0] == required:
            new_bridge = bridge + [p]
            bridges.add(tuple(new_bridge))
            build(new_bridge, remaining(parts, p), p[1], bridges)
        elif p[1] == required:
            new_bridge = bridge + [p]
            bridges.add(tuple(new_bridge))
            build(new_bridge, remaining(parts, p), p[0], bridges)

def build_bridges(parts):
    bridges = set()
    build([], parts, 0, bridges)
    return bridges
    
def part1(bridges):
    strongest = 0
    for bridge in bridges:
        strongest = max(strongest, strength(bridge))
    print(strongest)

def part2(bridges):
    longest = 0
    for bridge in bridges:
        longest = max(longest, len(bridge))
    longest_bridges = [bridge for bridge in bridges if len(bridge) == longest]
    strongest = 0
    for bridge in longest_bridges:
        strongest = max(strongest, strength(bridge))
    print(strongest)
    
with open('../input/24.txt') as f:
    parts = []
    for line in f.readlines():
        a, b = line.strip().split('/')
        parts.append((int(a), int(b)))

bridges = build_bridges(parts)
part1(bridges)
part2(bridges)
