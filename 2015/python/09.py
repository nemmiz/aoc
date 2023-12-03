#!/usr/bin/python3

from itertools import permutations

distances = {}
with open('../input/09.txt') as f:
    for line in f.readlines():
        parts = line.split()
        if parts[0] not in distances:
            distances[parts[0]] = {}
        if parts[2] not in distances:
            distances[parts[2]] = {}
        distances[parts[0]][parts[2]] = int(parts[4])
        distances[parts[2]][parts[0]] = int(parts[4])

shortest = 10e9
longest = 0

for p in permutations(distances.keys()):
    distance = 0
    for i in range(1, len(p)):
        distance += distances[p[i-1]][p[i]]
    shortest = min(distance, shortest)
    longest = max(distance, longest)

print(shortest)
print(longest)
