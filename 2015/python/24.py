#!/usr/bin/python3

from itertools import combinations
from functools import reduce
import operator

def calculate(packages, groups):
    total_weight = sum(packages)
    group_weight = total_weight // groups

    for i in range(1, len(packages)):
        candidates = [p for p in combinations(packages, i) if sum(p) == group_weight]
        if candidates:
            break

    quantum_entanglements = [reduce(operator.mul, x) for x in candidates]
    print(min(quantum_entanglements))

with open('../input/24.txt') as f:
    packages = [int(line) for line in f.readlines()]

calculate(packages, 3)
calculate(packages, 4)
