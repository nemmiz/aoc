#!/usr/bin/python3

from itertools import permutations

def calculate_happiness(effects):
    best = -10e9
    for p in permutations(effects.keys()):
        happiness = 0
        for i in range(len(p)):
            happiness += effects[p[i]][p[(i+1)%len(p)]]
            happiness += effects[p[i]][p[(i-1)%len(p)]]
        best = max(best, happiness)
    print(best)

effects = {}
with open('../input/13.txt') as f:
    for line in f.readlines():
        person, _, gain_or_lose, amount, _, _, _, _, _, _, neighbor = line.split()
        amount = int(amount) if gain_or_lose == 'gain' else -int(amount)
        neighbor = neighbor.rstrip('.')
        if person not in effects:
            effects[person] = {}
        effects[person][neighbor] = amount

calculate_happiness(effects)

for neighbors in effects.values():
    neighbors['Myself'] = 0
effects['Myself'] = {person: 0 for person in effects.keys()}
calculate_happiness(effects)
