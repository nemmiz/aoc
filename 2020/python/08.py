def execute(instructions):
    acc = 0
    pc = 0
    visited = set()
    plen = len(instructions)
    while True:
        if pc in visited:
            return acc, False
        if pc >= plen:
            return acc, True
        visited.add(pc)
        op, arg = instructions[pc]
        if op == 'acc':
            acc += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        elif op == 'nop':
            pc += 1

def part1(instructions):
    acc, _ = execute(instructions)
    print(acc)

def part2(instructions):
    mod_index = -1
    mod_instructions = []
    switches = {'nop': 'jmp', 'jmp': 'nop'}
    while True:
        while True:
            mod_index += 1
            op, arg = instructions[mod_index]
            if op in switches:
                mod_instructions = instructions.copy()
                mod_instructions[mod_index] = (switches[op], arg)
                break
        acc, terminated = execute(mod_instructions)
        if terminated:
            print(acc)
            break

with open('../input/08.txt') as stream:
    instructions = []
    for line in stream:
        op, arg = line.split()
        arg = int(arg)
        instructions.append((op, arg))

part1(instructions)
part2(instructions)
