def step(east_facing, south_facing, w, h):
    new_east_facing = set()
    for pos in east_facing:
        new_pos = (0 if pos[0] >= w else pos[0]+1, pos[1])
        if new_pos not in east_facing and new_pos not in south_facing:
            new_east_facing.add(new_pos)
        else:
            new_east_facing.add(pos)

    new_south_facing = set()
    for pos in south_facing:
        new_pos = (pos[0], 0 if pos[1] >= h else pos[1]+1)
        if new_pos not in new_east_facing and new_pos not in south_facing:
            new_south_facing.add(new_pos)
        else:
            new_south_facing.add(pos)

    return new_east_facing, new_south_facing

def move(east_facing, south_facing, w, h):
    steps = 0
    while True:
        steps += 1
        new_east_facing, new_south_facing = step(east_facing, south_facing, w, h)
        if new_east_facing == east_facing and new_south_facing == south_facing:
            print(steps)
            return
        east_facing, south_facing = new_east_facing, new_south_facing

with open('../input/25.txt') as stream:
    initial_east_facing = set()
    initial_south_facing = set()
    width, height = 0, 0
    for y, line in enumerate(stream.readlines()):
        line = line.strip()
        width = max(width, len(line)-1)
        height = max(height, y)
        for x, c in enumerate(line):
            if c == '>':
                initial_east_facing.add((x, y))
            elif c == 'v':
                initial_south_facing.add((x, y))

move(initial_east_facing, initial_south_facing, width, height)
