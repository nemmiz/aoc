#!/usr/bin/python3

from itertools import count

def part1(inp):
    houses = [0] * (inp // 30)

    for i in range(1, len(houses)):
        for j in range(i, len(houses), i):
            houses[j] += (i*10)

    for i, presents in enumerate(houses):
        if presents >= inp:
            print(i)
            break

def part2(inp):
    houses = {}

    for elf in count(1):
        for i in range(1, 51):
            house_index = elf * i
            presents = houses.get(house_index, 0)
            presents += elf * 11
            houses[house_index] = presents

        if houses[elf] >= inp:
            print(elf)
            break

puzzle_input = 29000000
part1(puzzle_input)
part2(puzzle_input)
