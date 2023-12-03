#!/usr/bin/python3

import sys
from itertools import permutations
from collections import deque

def part1(nodeinfo):
    total = 0
    for a, b in permutations(nodeinfo, 2):
        if a[3] == 0:
            continue
        if a[3] > b[4]:
            continue
        total += 1
    print(total)

def part2(nodeinfo):
    # Take the size of a known "good" node (0, 0)
    for x, y, size, _, _ in nodeinfo:
        if x == 0 and y == 0:
            min_size = size
            max_size = size
            huge_size = size * 2
            break

    # Find the position of the empty node
    for x, y, _, used, _ in nodeinfo:
        if used == 0:
            empty_x = x
            empty_y = y
            break

    interchangable_nodes = set()
    goal_x, goal_y = 0, 0

    # Find the goal data node and build the set of interchangable nodes
    for x, y, size, used, _ in nodeinfo:
        if used < huge_size:
            min_size = min(min_size, size)
            max_size = max(max_size, size)
            goal_x = max(goal_x, x)
            if used > min_size:
                sys.exit('Something is not right here')
            else:
                interchangable_nodes.add((x, y))

    queue = deque([(empty_x, empty_y, goal_x, goal_y)])
    neighbors = ((0, -1), (0, 1), (-1, 0), (1, 0))
    visited_states = {queue[0]: 0}

    while queue:
        state = queue.popleft()
        empty_x, empty_y, goal_x, goal_y = state

        if goal_x == 0 and goal_y == 0:
            print(visited_states[state])
            break

        for offset_x, offset_y in neighbors:
            neighbor_x = empty_x + offset_x
            neighbor_y = empty_y + offset_y
            if (neighbor_x, neighbor_y) not in interchangable_nodes:
                continue
            if neighbor_x == goal_x and neighbor_y == goal_y:
                new_state = (neighbor_x, neighbor_y, empty_x, empty_y)
            else:
                new_state = (neighbor_x, neighbor_y, goal_x, goal_y)
            if new_state not in visited_states:
                queue.append(new_state)
                visited_states[new_state] = visited_states[state]+1


with open('../input/22.txt') as f:
    nodeinfo = []
    for i, line in enumerate(f.readlines()):
        if i >= 2:
            parts = line.replace('-x', ' ').replace('-y', ' ').split()
            nodeinfo.append((int(parts[1]), int(parts[2]), int(parts[3][:-1]), int(parts[4][:-1]), int(parts[5][:-1])))

part1(nodeinfo)
part2(nodeinfo)
