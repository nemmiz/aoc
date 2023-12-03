#!/usr/bin/python3

import sys
from itertools import count


def run(instructions, regs):
    pc = 0
    while pc < len(instructions):
        inst = instructions[pc]
        if inst[0] == 'cpy':
            if inst[1] in 'abcd':
                src = regs[inst[1]]
            else:
                src = int(inst[1])
            regs[inst[2]] = src
            pc += 1
        elif inst[0] == 'inc':
            regs[inst[1]] += 1
            pc += 1
        elif inst[0] == 'dec':
            regs[inst[1]] -= 1
            pc += 1
        elif inst[0] == 'jnz':
            if inst[1] in 'abcd':
                src = regs[inst[1]]
            else:
                src = int(inst[1])
            if src != 0:
                pc += int(inst[2])
            else:
                pc += 1
        elif inst[0] == 'out':
            yield regs[inst[1]]
            pc += 1
    print(regs['a'])


def solve(instructions):
    for i in count():
        expected = 0
        for j, x in enumerate(run(instructions, {'a': i, 'b': 0, 'c': 0, 'd': 0})):
            if x != expected:
                break
            expected ^= 1
            if j == 100:
                print(i)
                return


with open('../input/25.txt') as f:
    instructions = [line.split() for line in f.readlines()]

solve(instructions)
