#!/usr/bin/python3


def set_grid(grid, value, sx, sy, ex, ey):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            grid[y*1000+x] = value

def toggle_grid(grid, sx, sy, ex, ey):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            grid[y*1000+x] = 0 if grid[y*1000+x] == 1 else 1

def inc_grid(grid, amount, sx, sy, ex, ey):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            grid[y*1000+x] += amount

def dec_grid(grid, amount, sx, sy, ex, ey):
    for y in range(sy, ey+1):
        for x in range(sx, ex+1):
            grid[y*1000+x] = max(0, grid[y*1000+x]-amount)


with open('../input/06.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

grid = bytearray(1000*1000)
grid2 = bytearray(1000*1000)
for instruction in instructions:
    if instruction.startswith('turn '):
        instruction = instruction[5:]
    parts = instruction.split()
    sx, sy = (int(x) for x in parts[1].split(','))
    ex, ey = (int(x) for x in parts[3].split(','))
    if instruction.startswith('off'):    
        set_grid(grid, 0, sx, sy, ex, ey)
        dec_grid(grid2, 1, sx, sy, ex, ey)
    elif instruction.startswith('on'):
        set_grid(grid, 1, sx, sy, ex, ey)
        inc_grid(grid2, 1, sx, sy, ex, ey)
    elif instruction.startswith('toggle'):
        toggle_grid(grid, sx, sy, ex, ey)
        inc_grid(grid2, 2, sx, sy, ex, ey)

print(grid.count(1))
print(sum(grid2))