#!/usr/bin/python3

import sys

def find_unbalanced(node, parents, children, weights):
    child_weights = []
    for child in children[node]:
        child_weights.append(find_unbalanced(child, parents, children, weights))
    unique = set(child_weights)
    if len(unique) == 2:
        expected, actual = sorted(unique)
        print(weights[children[node][child_weights.index(actual)]] - (actual - expected))
        sys.exit()
    return weights[node] + sum(child_weights)

with open('../input/07.txt') as f:
    parents = {}
    children = {}
    weights = {}
    for line in f.readlines():
        parts = line.replace(',', '').split()
        weights[parts[0]] = int(parts[1][1:-1])
        children[parts[0]] = []
        for child in parts[3:]:
            parents[child] = parts[0]
            children[parts[0]].append(child)

for tower in children:
    if tower not in parents:
        bottom_program = tower
        break

print(bottom_program)
print(find_unbalanced(bottom_program, parents, children, weights))
        
