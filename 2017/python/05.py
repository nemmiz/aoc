#!/usr/bin/python3

def part1(nums):
    nums = nums.copy()
    pos, steps = 0, 0
    while pos >= 0 and pos < len(nums):
        old = pos
        pos += nums[pos]
        nums[old] += 1
        steps += 1
    print(steps)

def part2(nums):
    nums = nums.copy()
    pos, steps = 0, 0
    while pos >= 0 and pos < len(nums):
        old = pos
        pos += nums[pos]
        if nums[old] >= 3:
            nums[old] -= 1
        else:
            nums[old] += 1
        steps += 1
    print(steps)

with open('../input/05.txt') as f:
    nums = [int(line) for line in f.readlines()]

part1(nums)
part2(nums)
