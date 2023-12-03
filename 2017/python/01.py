#!/usr/bin/python3

with open('../input/01.txt') as f:
    nums = list(map(int, f.read()))
    total1, total2, n = 0, 0, len(nums)
    for i, num in enumerate(nums):
        if num == nums[(i+1)%n]:
            total1 += nums[i]
        if num == nums[(i+n//2)%n]:
            total2 += nums[i]
    print(total1, total2, sep='\n')
