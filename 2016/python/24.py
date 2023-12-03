#!/usr/bin/python3

from itertools import permutations
from collections import deque

def solve(lines):
    numbers = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in '0123456789':
                numbers[(x, y)] = int(c)

    neighbors = ((0, -1), (0, 1), (-1, 0), (1, 0))
    distances = {}

    for start, n in numbers.items():
        queue = deque([start])
        visited = {start: 0}

        while queue:
            pos = queue.popleft()
            for dx, dy in neighbors:
                new_x = pos[0] + dx
                new_y = pos[1] + dy
                if lines[new_y][new_x] != '#':
                    new_pos = (new_x, new_y)
                    if new_pos not in visited:
                        visited[new_pos] = visited[pos]+1
                        queue.append(new_pos)

        tmp_dists = {}
        for pos, n2 in numbers.items():
            if n2 != n:
                tmp_dists[n2] = visited[pos]
        distances[n] = tmp_dists

    numbers_without_zero = list(numbers.values())
    numbers_without_zero.remove(0)
    min_dist = 10e9
    min_dist_with_return = 10e9

    for permutation in permutations(numbers_without_zero):
        dist = 0
        for i, n in enumerate(permutation):
            if i == 0:
                dist += distances[0][permutation[0]]
            else:
                dist += distances[permutation[i-1]][permutation[i]]
        min_dist = min(min_dist, dist)
        dist += distances[permutation[-1]][0]
        min_dist_with_return = min(min_dist_with_return, dist)

    print(min_dist)
    print(min_dist_with_return)


with open('../input/24.txt') as f:
    lines = [line.strip() for line in f.readlines()]

solve(lines)
