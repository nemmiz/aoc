#!/usr/bin/python3

def part1(step):
    state = [0]
    pos = 0
    for i in range(1, 2018):
        pos = (pos + step) % len(state) + 1
        state.insert(pos, i)
    print(state[pos+1])

def part2(step):
    pos = 0
    value = 0
    for i in range(1, 50000001):
        pos = (pos + step) % i + 1
        if pos == 1:
            value = i
    print(value)

part1(316)
part2(316)
