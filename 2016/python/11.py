#!/usr/bin/python3

from collections import deque
from itertools import combinations
    

def calculate_valid_states(n):
    """
    Given an initial state of size n, this will return a set of
    all possible valid states with the same size
    """

    def valid(arr, generators_on_floors):
        it = iter(arr)
        for a, b in zip(it, it):
            if a != b and generators_on_floors[b] != 0:
                return False
        return True

    def inner(arr, n, floors, generators_on_floors, ok):
        for a in floors:
            for b in floors:
                if a == b or generators_on_floors[b] == 0:
                    arr[n-2] = a
                    arr[n-1] = b
           
                    generators_on_floors[a] += 1
                    if n > 2:
                        inner(arr, n-2, floors, generators_on_floors, ok)
                    else:
                        if valid(arr, generators_on_floors):
                            ok.add(bytes(arr))
                    generators_on_floors[a] -= 1

    ok = set()
    inner(bytearray(n), n, (1, 2, 3, 4), bytearray([0, 0, 0, 0, 0]), ok)
    return ok


def solve(initial_state):
    floors = (1, 2, 3, 4)
    queue = deque([(initial_state, 0, 1)])
    end_state = bytes(floors[-1] for _ in initial_state)
    valid_states = calculate_valid_states(len(initial_state))
    states = [{}, {}, {}, {}, {}]

    while queue:
        state, steps, current_floor = queue.popleft()
        
        # Skip if we've been in this state before
        if state in states[current_floor]:
            continue
            
        states[current_floor][state] = steps
        items_here = [i for i, item in enumerate(state) if item == current_floor]

        for next_floor in (current_floor-1, current_floor+1):
            if next_floor not in floors:
                continue

            for a in items_here:
                new_state = bytearray(state)
                new_state[a] = next_floor
                new_state = bytes(new_state)
                if new_state in valid_states:
                    if new_state not in states[next_floor]:
                        queue.append((new_state, steps+1, next_floor))
                
            for a, b in combinations(items_here, 2):
                new_state = bytearray(state)
                new_state[a] = next_floor
                new_state[b] = next_floor
                new_state = bytes(new_state)
                if new_state in valid_states:
                    if new_state not in states[next_floor]:
                        queue.append((new_state, steps+1, next_floor))
                    
    print(states[4][end_state])


with open('../input/11.txt') as f:
    items = []
    for floor, line in enumerate(f.readlines()):
        parts = line.replace(',', '').replace('.', '').split()
        for i, p in enumerate(parts):
            if p == 'microchip':
                items.append((parts[i-1][:2].upper()+'M', floor+1))
            if p == 'generator':
                items.append((parts[i-1][:2].upper()+'G', floor+1))
    items.sort()
    state = bytes((index for _, index in items))

# Part 1
solve(state)

# Part 2 (add 4 more items to the first floor)
state += bytes((1, 1, 1, 1))
solve(state)
