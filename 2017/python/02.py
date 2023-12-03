#!/usr/bin/python3

from itertools import permutations

with open('../input/02.txt') as f:
    total1, total2 = 0, 0
    for line in f.readlines():
        nums = list(map(int, line.split()))
        total1 += (max(nums) - min(nums))
        for a, b in permutations(nums, 2):
            d, m = divmod(a, b)
            if m == 0:
                total2 += d
    print(total1, total2, sep='\n')
