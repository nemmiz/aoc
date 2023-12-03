#!/usr/bin/python3

def move(position, direction):
    if direction == '^':
        return (position[0], position[1]-1)
    elif direction == 'v':
        return (position[0], position[1]+1)
    elif direction == '<':
        return (position[0]-1, position[1])
    elif direction == '>':
        return (position[0]+1, position[1])

def part1(directions):
    position = (0, 0)
    houses = set([position])
    for direction in directions:
        position = move(position, direction)
        houses.add(position)
    print(len(houses))

def part2(directions):
    it = iter(directions)
    directions = zip(it, it)
    santa, robosanta = (0, 0), (0, 0)
    houses = set([santa])
    for dir1, dir2 in directions:
        santa = move(santa, dir1)
        houses.add(santa)
        robosanta = move(robosanta, dir2)
        houses.add(robosanta)
    print(len(houses))

with open('../input/03.txt') as f:
    directions = f.read()

part1(directions)
part2(directions)
