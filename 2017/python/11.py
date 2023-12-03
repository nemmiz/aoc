#!/usr/bin/python3


def solve(directions):
    simplifications = {
        'n': (('s', None), ('se', 'ne'), ('sw', 'nw')),
        's': (('n', None), ('ne', 'se'), ('nw', 'sw')),
        'ne': (('sw', None), ('s', 'se'), ('nw', 'n')),
        'se': (('nw', None), ('n', 'ne'), ('sw', 's')),
        'nw': (('se', None), ('s', 'sw'), ('ne', 'n')),
        'sw': (('ne', None), ('n', 'nw'), ('se', 's')),
    }
    steps_taken = {'n': 0, 's': 0, 'ne': 0, 'se': 0, 'nw': 0, 'sw': 0}
    furthest = 0
    for d in directions:
        for d2, replace in simplifications[d]:
            if steps_taken[d2] > 0:
                steps_taken[d2] -= 1
                if replace:
                    steps_taken[replace] += 1
                break
        else:
            steps_taken[d] += 1
        furthest = max(furthest, sum(steps_taken.values()))

    print(sum(steps_taken.values()))
    print(furthest)


with open('../input/11.txt') as f:
    solve(f.read().split(','))
