OFFSETS = {
    'e': (1, -1, 0),
    'se': (0, -1, 1),
    'sw': (-1, 0, 1),
    'w': (-1, 1, 0),
    'nw': (0, 1, -1),
    'ne': (1, 0, -1)
}

def position(steps):
    steps = list(reversed(steps))
    x, y, z = 0, 0, 0
    while steps:
        step = steps.pop()
        if step in 'ns':
            step = step + steps.pop()
        offset = OFFSETS[step]
        x += offset[0]
        y += offset[1]
        z += offset[2]
    return x, y, z
            
def add_neighbors(positions):
    tiles = {pos: 1 for pos in positions}
    for pos in positions:
        for offset in OFFSETS.values():
            neighbor = (pos[0] + offset[0], pos[1] + offset[1], pos[2] + offset[2])
            if neighbor not in tiles:
                tiles[neighbor] = 0
    return tiles

def count_neighbors(pos, grid):
    n = 0
    for offset in OFFSETS.values():
        tmp = (pos[0] + offset[0], pos[1] + offset[1], pos[2] + offset[2])
        n += grid.get(tmp, 0)
    return n

def simulate(black_tiles):
    all_tiles = add_neighbors(black_tiles)
    new_tiles = {}
    for pos, color in all_tiles.items():
        n = count_neighbors(pos, all_tiles)
        if color == 1 and (n == 0 or n > 2):
            color = 0
        elif color == 0 and n == 2:
            color = 1
        new_tiles[pos] = color
    return {pos for pos, color in new_tiles.items() if color == 1}

with open('../input/24.txt') as stream:
    lines = [line.strip() for line in stream]

black_tiles = set()
for steps in lines:
    pos = position(steps)
    if pos in black_tiles:
        black_tiles.remove(pos)
    else:
        black_tiles.add(pos)
print(len(black_tiles))

for i in range(100):
    black_tiles = simulate(black_tiles)
print(len(black_tiles))
