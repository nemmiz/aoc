#!/usr/bin/python3

import operator

with open('../input/08.txt') as f:
    instructions = []
    for line in f.readlines():
        tmp = line.split()
        instructions.append((tmp[0], tmp[1], int(tmp[2]), tmp[4], tmp[5], int(tmp[6])))

regs = {}
highest_ever = 0
ops = {
    '>': operator.gt,
    '<': operator.lt,
    '>=': operator.ge,
    '<=': operator.le,
    '==': operator.eq,
    '!=': operator.ne,
}

for reg1, inc_or_dec, amt1, reg2, op, amt2 in instructions:
    if reg1 not in regs:
        regs[reg1] = 0
    if reg2 not in regs:
        regs[reg2] = 0

    if ops[op](regs[reg2], amt2):
        if inc_or_dec == 'inc':
            regs[reg1] += amt1
        elif inc_or_dec == 'dec':
            regs[reg1] -= amt1

    highest_ever = max(highest_ever, max(regs.values()))

print(max(regs.values()))
print(highest_ever)
