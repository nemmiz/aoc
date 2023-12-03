#!/usr/bin/python3

import sys


def add_2x2_rule(src, dst, rules):
    pattern = tuple(src.replace('/', ''))
    result = tuple(dst.replace('/', ''))
    # Rotate
    pat = pattern
    for _ in range(4):
        rules[pat] = result
        pat = (pat[2], pat[0], pat[3], pat[1])
    # Vertical flip and rotate
    pat = pattern[2:] + pattern[:2]
    for _ in range(4):
        rules[pat] = result
        pat = (pat[2], pat[0], pat[3], pat[1])
    # Horizontal flip and rotate
    pat = (pattern[1], pattern[0], pattern[3], pattern[2])
    for _ in range(4):
        rules[pat] = result
        pat = (pat[2], pat[0], pat[3], pat[1])


def add_3x3_rule(src, dst, rules):
    pattern = tuple(src.replace('/', ''))
    result = tuple(dst.replace('/', ''))
    # Rotate
    pat = pattern
    for _ in range(4):
        rules[pat] = result
        pat = (pat[6], pat[3], pat[0], pat[7], pat[4], pat[1], pat[8], pat[5], pat[2])
    # Vertical flip and rotate
    pat = pattern[6:] + pattern[3:6] + pattern[:3]
    for _ in range(4):
        rules[pat] = result
        pat = (pat[6], pat[3], pat[0], pat[7], pat[4], pat[1], pat[8], pat[5], pat[2])
    # Horizontal flip and rotate
    pat = (pattern[2], pattern[1], pattern[0], pattern[5], pattern[4], pattern[3], pattern[8], pattern[7], pattern[6])
    for _ in range(4):
        rules[pat] = result
        pat = (pat[6], pat[3], pat[0], pat[7], pat[4], pat[1], pat[8], pat[5], pat[2])


def add_rule(rule, rules):
    src, dst = rule.split(' => ')
    if len(src) == 5:
        add_2x2_rule(src, dst, rules)
    elif len(src) == 11:
        add_3x3_rule(src, dst, rules)


def next_grid(grid, size, rules):
    if size % 2 == 0:
        new_grid = []
        for y in range(0, size, 2):
            results = []
            for x in range(0, size, 2):
                rule = (
                    grid[(x+0)+(y+0)*size], grid[(x+1)+(y+0)*size],
                    grid[(x+0)+(y+1)*size], grid[(x+1)+(y+1)*size],
                )
                result = rules[rule]
                results.append(result)
            for r in results:
                new_grid.extend(r[0:3])
            for r in results:
                new_grid.extend(r[3:6])
            for r in results:
                new_grid.extend(r[6:9])
        return new_grid, size//2*3
    elif size % 3 == 0:
        new_grid = []
        for y in range(0, size, 3):
            results = []
            for x in range(0, size, 3):
                rule = (
                    grid[(x+0)+(y+0)*size], grid[(x+1)+(y+0)*size], grid[(x+2)+(y+0)*size],
                    grid[(x+0)+(y+1)*size], grid[(x+1)+(y+1)*size], grid[(x+2)+(y+1)*size],
                    grid[(x+0)+(y+2)*size], grid[(x+1)+(y+2)*size], grid[(x+2)+(y+2)*size],
                )
                result = rules[rule]
                results.append(result)
            for r in results:
                new_grid.extend(r[0:4])
            for r in results:
                new_grid.extend(r[4:8])
            for r in results:
                new_grid.extend(r[8:12])
            for r in results:
                new_grid.extend(r[12:16])
        return new_grid, size//3*4


with open('../input/21.txt') as f:
    rules = {}
    for line in f.readlines():
        add_rule(line.strip(), rules)

grid = tuple('.#...####')
size = 3

for i in range(18):
    grid, size = next_grid(grid, size, rules)
    if i in (4, 17):
        print(grid.count('#'))
