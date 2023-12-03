#!/usr/bin/python3

def dance(programs, moves):
    for move in moves:
        if move[0] == 's':
            size = move[1]
            programs = programs[-size:] + programs[:-size]
        elif move[0] == 'x':
            pos1 = move[1]
            pos2 = move[2]
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
        elif move[0] == 'p':
            pos1 = programs.index(move[1])
            pos2 = programs.index(move[2])
            programs[pos1], programs[pos2] = programs[pos2], programs[pos1]
    return programs


def part1(moves):
    programs = list('abcdefghijklmnop')
    programs = dance(programs, moves)
    print(''.join(programs))


def part2(moves):
    programs = list('abcdefghijklmnop')
    states = [tuple(programs)]

    while True:
        programs = dance(programs, moves)
        state = tuple(programs)
        if state == states[0]:
            break
        states.append(state)

    for i in range(1, len(states)):
        programs = dance(programs, moves)
        state = tuple(programs)
        assert(states[i] == state)

    idx = 1000000000 % len(states)
    print(''.join(states[idx]))


with open('../input/16.txt') as f:
    moves = []
    tmp = f.read().split(',')
    for t in tmp:
        cmd = t[0]
        if t[0] == 's':
            moves.append(('s', int(t[1:])))
        elif t[0] == 'x':
            a, b = tuple(int(x) for x in t[1:].split('/'))
            moves.append(('x', a, b))
        elif t[0] == 'p':
            a, b = tuple(x for x in t[1:].split('/'))
            moves.append(('p', a, b))

part1(moves)
part2(moves)
