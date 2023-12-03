#!/usr/bin/python3

from itertools import count

def solve(starts, nums):
    for i in count():
        n = len(starts)

        start_time = i
        current_time = start_time
        end_time = start_time + n

        while current_time < end_time:
            current_time += 1
            delta_time = current_time - start_time
            disc = delta_time - 1
            disc_pos = (starts[disc] + current_time) % nums[disc]
        
            if disc_pos != 0:
                break
        else:
            return start_time

with open('../input/15.txt') as f:
    num_positions = []
    start_positions = []
    for line in f.readlines():
        parts = line.rstrip('\n.').split()
        num_positions.append(int(parts[3]))
        start_positions.append(int(parts[-1]))
    num_positions = tuple(num_positions)
    start_positions = tuple(start_positions)

print(solve(start_positions, num_positions))
print(solve(start_positions + (0,), num_positions + (11,)))
