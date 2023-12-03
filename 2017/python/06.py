#!/usr/bin/python3

from itertools import count

def solve(nums):
    nums = nums.copy()
    states = {tuple(nums): 0}
    for cycles in count():
        blocks = max(nums)
        i = nums.index(blocks)
        nums[i] = 0
        while blocks > 0:
            i = (i + 1) % len(nums)
            nums[i] += 1
            blocks -= 1
        t = tuple(nums)
        if t in states:
            print(cycles+1)
            print(cycles-states[t])
            break
        states[t] = cycles

with open('../input/06.txt') as f:
    solve(list(map(int, f.read().split())))
