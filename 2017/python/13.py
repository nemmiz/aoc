#!/usr/bin/python3

from itertools import count

def scanner_at_0(elapsed, r):
    cycle = (r-1)<<1
    return (elapsed % cycle) == 0

def severity(scanners, delay):
    total = 0
    for depth, r in scanners:
        elapsed = depth + delay
        if scanner_at_0(elapsed, r):
            total += (depth * r)
    return total

def caught(scanners, delay):
    for depth, r in scanners:
        elapsed = depth + delay
        if scanner_at_0(elapsed, r):
            return True
    return False

def part1(scanners):
    print(severity(scanners, 0))

def part2(scanners):
    for i in count():
        if not caught(scanners, i):
            print(i)
            break


with open('../input/13.txt') as f:
    scanners = [tuple(int(x) for x in line.strip().split(': ')) for line in f.readlines()]

part1(scanners)
part2(scanners)
