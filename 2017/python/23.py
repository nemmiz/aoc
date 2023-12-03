#!/usr/bin/python3

from string import ascii_lowercase


def part1(instructions, regs):
    regs = regs.copy()
    ip = 0
    mul_calls = 0
    while ip < len(instructions):
        op, x, y = instructions[ip]
        if op == 'set':
            regs[x] = regs[y]
        elif op == 'sub':
            regs[x] -= regs[y]
        elif op == 'mul':
            regs[x] *= regs[y]
            mul_calls += 1
        elif op == 'jnz':
            if regs[x] != 0:
                ip += regs[y]
                ip -= 1
        ip += 1
    print(mul_calls)


def part2(instructions, regs):
    regs = regs.copy()
    regs['a'] = 1
    ip = 0
    while ip < len(instructions):
        op, x, y = instructions[ip]

        # Optimization #1
        # There's a tight loop at ip 11-19 that increments e until it equals b.
        # If d*e==b during this loop, set f to 0.
        if ip == 16:
            regs['e'] = regs['b'] - 1
            if regs['b'] % regs['d'] == 0:
                regs['f'] = 0

        # Optimization #2
        # Outer loop containing the loop in optimization 1. Loops until d equals b.
        # Also take into consideration the same condition as in optimization 1.
        elif ip == 20:
            while regs['d'] < (regs['b'] - 1):
                if regs['b'] % regs['d'] == 0:
                    regs['f'] = 0
                    break
                regs['d'] += 1
            regs['d'] = regs['b'] - 1

        if op == 'set':
            regs[x] = regs[y]
        elif op == 'sub':
            regs[x] -= regs[y]
        elif op == 'mul':
            regs[x] *= regs[y]
        elif op == 'jnz':
            if regs[x] != 0:
                ip += regs[y]
                ip -= 1
        ip += 1
    print(regs['h'])


with open('../input/23.txt') as f:
    regs = {}
    instructions = []
    for line in f.readlines():
        parts = line.split()
        for i in range(1, len(parts)):
            if parts[i] in ascii_lowercase:
                regs[parts[i]] = 0
            else:
                parts[i] = int(parts[i])
                regs[parts[i]] = parts[i]
        instructions.append(tuple(parts))

part1(instructions, regs)
part2(instructions, regs)
