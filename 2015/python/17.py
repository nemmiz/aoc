#!/usr/bin/python3

from itertools import combinations

with open('../input/17.txt') as f:
    containers = [int(line) for line in f.readlines()]

sums = []
for i in range(len(containers)+1):
    s = 0
    for c in combinations(containers, i):
        if sum(c) == 150:
            s += 1
    sums.append(s)

print(sum(sums))

for x in sums:
    if x != 0:
        print(x)
        break
