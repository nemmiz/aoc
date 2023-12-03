#!/usr/bin/python3

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
    print(regs['a'])

with open('../input/12.txt') as f:
    instructions = [line.split() for line in f.readlines()]

run(instructions, {'a': 0, 'b': 0, 'c': 0, 'd': 0})
run(instructions, {'a': 0, 'b': 0, 'c': 1, 'd': 0})
