#!/usr/bin/python3

def run(instructions, regs):
    pc = 0

    while pc < len(instructions):
        instruction = instructions[pc]
        opcode = instruction[0]

        if opcode == 'hlf':
            regs[instruction[1]] //= 2
            pc += 1
        elif opcode == 'tpl':
            regs[instruction[1]] *= 3
            pc += 1
        elif opcode == 'inc':
            regs[instruction[1]] += 1
            pc += 1
        elif opcode == 'jmp':
            pc += int(instruction[1])
        elif opcode == 'jie':
            if regs[instruction[1]] % 2 == 0:
                pc += int(instruction[2])
            else:
                pc += 1
        elif opcode == 'jio':
            if regs[instruction[1]] == 1:
                pc += int(instruction[2])
            else:
                pc += 1
        else:
            print('Unknown opcode', opcode)
            break

    print(regs)


with open('../input/23.txt') as f:
    instructions = [line.replace(',', '').split() for line in f.readlines()]

run(instructions, regs={'a': 0, 'b': 0})
run(instructions, regs={'a': 1, 'b': 0})
