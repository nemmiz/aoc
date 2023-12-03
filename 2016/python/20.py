#!/usr/bin/python3

def merge_ranges(ranges):
    i = 0
    new_ranges = []
    while i < len(ranges)-1:
        min1, max1 = ranges[i]
        min2, max2 = ranges[i+1]
        if min2 <= max1+1:
            min3 = min1
            max3 = max(max1, max2)
            ranges[i] = (min3, max3)
            del ranges[i+1]
        else:
            i += 1

def count_allowed_ips(ranges):
    total = max(0, ranges[0][0]) + max(0, 4294967295-ranges[-1][1])
    for i in range(1, len(ranges)):
        total += (ranges[i][0] - ranges[i-1][1] - 1)
    return total


with open('../input/20.txt') as f:
    ranges = [tuple(map(int, line.split('-'))) for line in f.readlines()]

ranges.sort()
merge_ranges(ranges)

print(ranges[0][1]+1)
print(count_allowed_ips(ranges))
