#!/usr/bin/python3

facts = {
    'children': 3,
    'cats': 7,
    'samoyeds': 2,
    'pomeranians': 3,
    'akitas': 0,
    'vizslas': 0,
    'goldfish': 5,
    'trees': 3,
    'cars': 2,
    'perfumes': 1,
}

sues = []
with open('../input/16.txt') as f:
    for line in f.readlines():
        parts = line.split()
        properties = [part.rstrip(':') for part in parts[2::2]]
        values = [int(part.rstrip(',')) for part in parts[3::2]]
        sues.append(dict(zip(properties, values)))

for i, sue in enumerate(sues):
    for prop, value in sue.items():
        if facts[prop] != value:
            break
    else:
        print('Sue', i+1, 'matches!')

for i, sue in enumerate(sues):
    for prop, value in sue.items():
        if prop in ('cats', 'trees'):
            if facts[prop] >= value:
                break
        elif prop in ('pomeranians', 'goldfish'):
            if facts[prop] <= value:
                break
        else:
            if facts[prop] != value:
                break
    else:
        print('Sue', i+1, 'matches!')
