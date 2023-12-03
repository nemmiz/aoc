#!/usr/bin/python3

from copy import deepcopy


def run(instructions, regs):
    instructions = deepcopy(instructions)
    pc = 0
    while pc < len(instructions):

        # Detect a = b * c
        if pc < len(instructions)-8:
            if (instructions[pc+0][0] == 'cpy' and
                instructions[pc+1][0] == 'cpy' and
                instructions[pc+2][0] == 'cpy' and
                instructions[pc+3][0] == 'inc' and
                instructions[pc+4][0] == 'dec' and
                instructions[pc+5][0] == 'jnz' and
                instructions[pc+6][0] == 'dec' and
                instructions[pc+7][0] == 'jnz' and
                instructions[pc+5][2] == '-2' and
                instructions[pc+7][2] == '-5'):
                factor_a_reg = instructions[pc+0][1]
                factor_b_reg = instructions[pc+2][1]
                product_reg = instructions[pc+3][1]
                regs[product_reg] = regs[factor_a_reg] * regs[factor_b_reg]
                regs[instructions[pc+4][1]] = 0
                regs[instructions[pc+6][1]] = 0
                pc += 8
                continue

        # Detect a += b
        if pc < len(instructions)-3:
            if (instructions[pc+0][0] == 'dec' and
                instructions[pc+1][0] == 'inc' and
                instructions[pc+2][0] == 'jnz' and
                instructions[pc+2][2] == '-2'):
                reg_a = instructions[pc+1][1]
                reg_b = instructions[pc+0][1]
                regs[reg_a] += regs[reg_b]
                regs[reg_b] = 0
                pc += 3
                continue
            elif (instructions[pc+0][0] == 'inc' and
                  instructions[pc+1][0] == 'dec' and
                  instructions[pc+2][0] == 'jnz' and
                  instructions[pc+2][2] == '-2'):
                reg_a = instructions[pc+0][1]
                reg_b = instructions[pc+1][1]
                regs[reg_a] += regs[reg_b]
                regs[reg_b] = 0
                pc += 3
                continue
        
        # Otherwise, execute as normal
        inst = instructions[pc]        

        if inst[0] == 'cpy':
            src = regs[inst[1]] if inst[1] in 'abcd' else int(inst[1])
            regs[inst[2]] = src
            pc += 1
        elif inst[0] == 'inc':
            regs[inst[1]] += 1
            pc += 1
        elif inst[0] == 'dec':
            regs[inst[1]] -= 1
            pc += 1
        elif inst[0] == 'jnz':
            src = regs[inst[1]] if inst[1] in 'abcd' else int(inst[1])
            dst = regs[inst[2]] if inst[2] in 'abcd' else int(inst[2])
            if src != 0:
                pc += dst
            else:
                pc += 1
        elif inst[0] == 'tgl':
            if inst[1] in 'abcd':
                idx = pc + regs[inst[1]]
            else:
                idx = pc + int(inst[1])
            if idx >= 0 and idx < len(instructions):
                old_inst = instructions[idx]
                if len(old_inst) == 2:
                    if old_inst[0] == 'inc':
                        instructions[idx] = ['dec'] + old_inst[1:]
                    else:
                        instructions[idx] = ['inc'] + old_inst[1:]
                elif len(old_inst) == 3:
                    if old_inst[0] == 'jnz':
                        instructions[idx] = ['cpy'] + old_inst[1:]
                    else:
                        instructions[idx] = ['jnz'] + old_inst[1:]
            pc += 1

    print(regs['a'])


with open('../input/23.txt') as f:
    instructions = [line.split() for line in f.readlines()]

run(instructions, {'a': 7, 'b': 0, 'c': 0, 'd': 0})
run(instructions, {'a': 12, 'b': 0, 'c': 0, 'd': 0})
