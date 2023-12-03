#!/usr/bin/python3

import sys
from string import ascii_lowercase
from collections import deque


def part1(instructions, regs):
    regs = regs.copy()
    last_played = 0
    ip = 0
    while ip < len(instructions):
        op, x, *y = instructions[ip]
        y = y[0] if y else None

        if op == 'set':
            regs[x] = regs[y]
        elif op == 'add':
            regs[x] += regs[y]
        elif op == 'mul':
            regs[x] *= regs[y]
        elif op == 'mod':
            regs[x] %= regs[y]
        elif op == 'jgz':
            if regs[x] > 0:
                ip += regs[y]
                ip -= 1
        elif op == 'snd':
            last_played = regs[x]
        elif op == 'rcv':
            if regs[x] != 0:
                print(last_played)
                break
        ip += 1


def make_program(instructions, regs):
    regs = regs.copy()
    ip = 0
    while ip < len(instructions):
        op, x, *y = instructions[ip]
        y = y[0] if y else None

        if op == 'set':
            regs[x] = regs[y]
        elif op == 'add':
            regs[x] += regs[y]
        elif op == 'mul':
            regs[x] *= regs[y]
        elif op == 'mod':
            regs[x] %= regs[y]
        elif op == 'jgz':
            if regs[x] > 0:
                ip += regs[y]
                ip -= 1
        elif op == 'snd':
            yield regs[x]
        elif op == 'rcv':
            value = yield None
            while value is None:
                value = yield None
            regs[x] = value
        ip += 1


def part2(instructions, regs):
    regsA = regs.copy()
    regsA['p'] = 0
    progA = make_program(instructions, regsA)
    queueA = deque()

    regsB = regs.copy()
    regsB['p'] = 1
    progB = make_program(instructions, regsB)
    queueB = deque()

    times = 0
    outA, outB = 0, 0

    while outA is not None or outB is not None:
        outA = next(progA)
        if outA is None:
            if queueA:
                outA = progA.send(queueA.popleft())
                if outA is not None:
                    queueB.append(outA)
        else:
            queueB.append(outA)

        outB = next(progB)
        if outB is None:
            if queueB:
                outB = progB.send(queueB.popleft())
                if outB is not None:
                    times += 1
                    queueA.append(outB)
        else:
            times += 1
            queueA.append(outB)

    print(times)


with open('../input/18.txt') as f:
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
