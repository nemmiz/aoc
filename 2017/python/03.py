#!/usr/bin/python3

def steps():
    n = 1
    while True:
        for i in range(n):
            yield 1, 0
        for i in range(n):
            yield 0, -1
        n += 1
        for i in range(n):
            yield -1, 0
        for i in range(n):
            yield 0, 1
        n += 1

def neighbors(x, y):
    yield (x-1, y-1)
    yield (x, y-1)
    yield (x+1, y-1)
    yield (x-1, y)
    yield (x+1, y)
    yield (x-1, y+1)
    yield (x, y+1)
    yield (x+1, y+1)

def part1(square):
    x, y = 0, 0
    for i, velocity in enumerate(steps()):
        if (i+1) == square:
            break
        x += velocity[0]
        y += velocity[1]
    print(abs(x)+abs(y))

def part2(puzzle_input):
    x, y = 0, 0
    squares = {(x, y): 1}
    for i, velocity in enumerate(steps()):
        x += velocity[0]
        y += velocity[1]
        value = sum((squares.get(neighbor, 0) for neighbor in neighbors(x, y)))
        squares[(x, y)] = value

        if value > puzzle_input:
            print(value)
            break

part1(312051)
part2(312051)
