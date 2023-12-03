def adjacent(pos):
    yield (pos[0]-1, pos[1]-1)
    yield (pos[0]  , pos[1]-1)
    yield (pos[0]+1, pos[1]-1)
    yield (pos[0]-1, pos[1]  )
    yield (pos[0]+1, pos[1]  )
    yield (pos[0]-1, pos[1]+1)
    yield (pos[0]  , pos[1]+1)
    yield (pos[0]+1, pos[1]+1)

def step(octopuses):
    for pos, energy in octopuses.items():
        octopuses[pos] = energy + 1

    flashed = set()
    while True:
        num_flashed = len(flashed)
        for pos, energy in octopuses.items():
            if energy > 9 and pos not in flashed:
                flashed.add(pos)
                for adj in adjacent(pos):
                    if adj in octopuses:
                        octopuses[adj] = octopuses[adj] + 1
        if len(flashed) == num_flashed:
            break

    for pos in flashed:
        octopuses[pos] = 0

    return len(flashed)

def part1(octopuses):
    octopuses = octopuses.copy()
    print(sum(step(octopuses) for _ in range(100)))

def part2(octopuses):
    octopuses = octopuses.copy()
    for i in range(1, 10**10):
        if step(octopuses) == 100:
            print(i)
            return

with open('../input/11.txt') as stream:
    octopuses = {}
    for y, line in enumerate(stream.readlines()):
        for x, c in enumerate(line.strip()):
            octopuses[(x, y)] = int(c)

part1(octopuses)
part2(octopuses)
