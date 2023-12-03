#!/usr/bin/python3

def generator(initial, factor):
    while True:
        initial *= factor
        initial %= 2147483647
        yield initial

def masked_generator(initial, factor, mask):
    while True:
        initial *= factor
        initial %= 2147483647
        if (initial & mask) == 0:
            yield initial

def part1(a, b):
    genA = generator(a, 16807)
    genB = generator(b, 48271)
    matches = 0
    for i in range(40000000):
        a = next(genA) & 0xffff
        b = next(genB) & 0xffff
        if a == b:
            matches += 1
    print(matches)

def part2(a, b):
    genA = masked_generator(a, 16807, 3)
    genB = masked_generator(b, 48271, 7)
    matches = 0
    for i in range(5000000):
        a = next(genA) & 0xffff
        b = next(genB) & 0xffff
        if a == b:
            matches += 1
    print(matches)

part1(116, 299)
part2(116, 299)
