#!/usr/bin/python3


def knot_hash(lengths, times):
    pos = 0
    skip = 0
    data = list(range(256))
    for _ in range(times):
        for length in lengths:
            i = pos
            tmp = []
            while len(tmp) != length:
                tmp.append(data[i%len(data)])
                i += 1
            tmp.reverse()
            i = pos
            for x in tmp:
                data[i%len(data)] = x
                i += 1
            pos = (pos + length + skip) % len(data)
            skip += 1
    return data
   

def part1(puzzle_input):
    lengths = [int(n) for n in puzzle_input.split(',')]
    data = knot_hash(lengths, 1)
    print(data[0]*data[1])


def part2(puzzle_input):
    lengths = [ord(c) for c in puzzle_input] + [17, 31, 73, 47, 23]
    sparse = knot_hash(lengths, 64)
    dense = []
    for i in range(0, len(sparse), 16):
        tmp = sparse[i]
        for j in range(i+1, i+16):
            tmp ^= sparse[j]
        dense.append(tmp)
    print(''.join(['{0:02x}'.format(x) for x in dense]))
        

with open('../input/10.txt') as f:
    puzzle_input = f.read()

part1(puzzle_input)
part2(puzzle_input)
