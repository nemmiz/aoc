def parse(line):
    if line.startswith('mask'):
        return line.split()[2]
    elif line.startswith('mem'):
        mem, _, value = line.split()
        return (int(mem[4:-1]), int(value))

def resolve_addresses(addr_bits):
    addresses = []
    def _rec(bits):
        if 'X' in bits:
            _rec(bits.replace('X', '0', 1))
            _rec(bits.replace('X', '1', 1))
        else:
            addresses.append(int(bits, 2))
    _rec(addr_bits)
    return addresses

def part1(instructions):
    mask = '0' * 36
    memory = {}
    for inst in instructions:
        if isinstance(inst, str):
            mask = inst
        else:
            addr, value = inst
            bits = '{0:036b}'.format(value)
            memory[addr] = int(''.join(a if a != 'X' else b for a, b in zip(mask, bits)), 2)
    print(sum(memory.values()))

def part2(instructions):
    mask = '0' * 36
    memory = {}
    for inst in instructions:
        if isinstance(inst, str):
            mask = inst
        else:
            addr, value = inst
            bits = '{0:036b}'.format(addr)
            floating_addr = ''.join(a if a in 'X1' else b for a, b in zip(mask, bits))
            addresses = resolve_addresses(floating_addr)
            for address in addresses:
                memory[address] = value
    print(sum(memory.values()))

with open('../input/14.txt') as stream:
    instructions = [parse(line) for line in stream]

part1(instructions)
part2(instructions)
