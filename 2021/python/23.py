from heapq import heappush, heappop
import sys

def remove_solved(state):
    for x, c in ((3, 'A'), (5, 'B'), (7, 'C'), (9, 'D')):
        for y in range(5, 1, -1):
            if (x, y+1) not in state and state.get((x, y)) == c:
                del state[(x, y)]

def is_solved(state):
    for x in range(3, 10, 2):
        for y in range(2, 6):
            if (x, y) in state:
                return False
    return True

def move_cost(state, from_pos, to_pos):
    x, y = from_pos
    xvel = 1 if to_pos[0] > x else -1
    yvel = 1 if to_pos[1] > y else -1
    steps = 0
    if y == 1:
        while x != to_pos[0]:
            steps += 1
            x += xvel
            if state.get((x, y)) != '.':
                return None
        while y != to_pos[1]:
            steps += 1
            y += yvel
            if state.get((x, y)) != '.':
                return None
    else:
        while y != to_pos[1]:
            steps += 1
            y += yvel
            if state.get((x, y)) != '.':
                return None
        while x != to_pos[0]:
            steps += 1
            x += xvel
            if state.get((x, y)) != '.':
                return None
    me = state.get(from_pos)
    if me == 'A':
        return steps
    if me == 'B':
        return steps * 10
    if me == 'C':
        return steps * 100
    if me == 'D':
        return steps * 1000
    return None

def room_target(state, x):
    for y in range(5, 1, -1):
        if (x, y) in state:
            return (x, y)
    return None

def valid_moves(state, pos):
    me = state.get(pos)
    if not me:
        return []
    x, y = pos
    if y == 1:
        if me == 'A':
            rt = room_target(state, 3)
        elif me == 'B':
            rt = room_target(state, 5)
        elif me == 'C':
            rt = room_target(state, 7)
        elif me == 'D':
            rt = room_target(state, 9)
        if rt is None:
            sys.exit('Bono my targets are gone!')
        if rt is not None:
            cost = move_cost(state, pos, rt)
            if cost is not None:
                return [(rt, cost)]
        return []
    else:
        targets = []
        for target in ((1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)):
            cost = move_cost(state, pos, target)
            if cost is not None:
                targets.append((target, cost))
        return targets
    
def const_state(state):
    tmp = []
    for k in sorted(state):
        tmp.append(k[0])
        tmp.append(k[1])
        tmp.append(state[k])
    return tuple(tmp)

def solve(initial_state):
    i = 0
    states = [(0, i, initial_state)]
    visited = {}

    while states:
        cost, _, state = heappop(states)

        if is_solved(state):
            print(cost)
            return
        
        cstate = const_state(state)
        if cstate in visited:
            if cost >= visited[cstate]:
                continue
        visited[cstate] = cost

        num_valid = 0
        for pos, c in state.items():
            if c in 'ABCD':
                moves = valid_moves(state, pos)
                num_valid += len(moves)

                for target, new_cost in moves:
                    i += 1
                    new_state = state.copy()
                    new_state[pos] = '.'
                    new_state[target] = c
                    remove_solved(new_state)
                    heappush(states, (cost+new_cost, i, new_state))

def parse(lines):
    state = {}
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c in '.ABCD':
                state[(x, y)] = c
    remove_solved(state)
    return state

with open('../input/23.txt') as stream:
    lines = stream.readlines()

# Part 1
solve(parse(lines))

# Part 2
lines.insert(3, '  #D#C#B#A#')
lines.insert(4, '  #D#B#A#C#')
solve(parse(lines))
