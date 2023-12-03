#!/usr/bin/python3

from collections import deque


def isopen(x, y):
    tmp = x*x + 3*x + 2*x*y + y + y*y + 1364
    return (bin(tmp).count('1') % 2 == 0)


def neighbors(point):
    points = (
        (point[0], point[1]-1),
        (point[0], point[1]+1),
        (point[0]-1, point[1]),
        (point[0]+1, point[1])
    )
    for x, y in points:
        if x >= 0 and y >= 0 and isopen(x, y):
            yield x, y


def find_path(start, goal):
    queue = deque([(start, 0)])
    came_from = {start: None}
    cost_so_far = {start: 0}

    while queue:
        pos, cost = queue.popleft()
        for neighbor in neighbors(pos):
            new_cost = cost_so_far[pos] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                queue.append((neighbor, new_cost))
                if neighbor == goal:
                    print(new_cost)
                    return


def find_reachable_points(start, max_steps):
    queue = deque([(start, 0)])
    cost_so_far = {start: 0}
    reachable_points = set()

    while queue:
        pos, cost = queue.popleft()
        if cost <= 50:
            reachable_points.add(pos)
        else:
            continue
        for neighbor in neighbors(pos):
            new_cost = cost_so_far[pos] + 1
            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = new_cost
                queue.append((neighbor, new_cost))

    print(len(reachable_points))
    

find_path(start=(1, 1), goal=(31, 39))
find_reachable_points(start=(1, 1), max_steps=50)
