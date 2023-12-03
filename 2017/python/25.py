#!/usr/bin/python3

def parse_input(lines):
    state = lines[0].split()[3].rstrip('.')
    steps = int(lines[1].split()[5])
    blueprint = {}
    for i in range(3, len(lines), 10):
        st = lines[i].split()[2].rstrip(':')
        write0 = 1 if '1' in lines[i+2] else 0
        write1 = 1 if '1' in lines[i+6] else 0
        move0 = 1 if 'right' in lines[i+3] else -1
        move1 = 1 if 'right' in lines[i+7] else -1
        next0 = lines[i+4].split()[4].rstrip('.')
        next1 = lines[i+8].split()[4].rstrip('.')
        blueprint[st] = ((write0, move0, next0), (write1, move1, next1))
    return state, steps, blueprint    

def solve(state, steps, blueprint):
    tape = {}
    pos = 0
    for i in range(steps):
        current = tape.get(pos, 0)
        value, move, next_state = blueprint[state][current]
        tape[pos] = value
        pos += move
        state = next_state
    print(sum(x for x in tape.values()))
    
with open('../input/25.txt') as f:
    state, steps, blueprint = parse_input(f.readlines())
    solve(state, steps, blueprint)
