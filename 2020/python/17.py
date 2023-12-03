from itertools import product

def positions(cubes):
    d = len(next(iter(cubes)))
    min_pos = [9999] * d
    max_pos = [-9999] * d
    for cube in cubes:
        for i, x in enumerate(cube):
            min_pos[i] = min(min_pos[i], x)
            max_pos[i] = max(max_pos[i], x)
    x = [range(a-1, b+2) for a, b in zip(min_pos, max_pos)]
    return product(*x)

def count_neighbors_3d(pos, cubes):
    n = 0
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            for z in range(pos[2]-1, pos[2]+2):
                if x == pos[0] and y == pos[1] and z == pos[2]:
                    continue
                if (x, y, z) in cubes:
                    n += 1
                    if n > 3:
                        return n
    return n

def count_neighbors_4d(pos, cubes):
    n = 0
    for x in range(pos[0]-1, pos[0]+2):
        for y in range(pos[1]-1, pos[1]+2):
            for z in range(pos[2]-1, pos[2]+2):
                for w in range(pos[3]-1, pos[3]+2):
                    if x == pos[0] and y == pos[1] and z == pos[2] and w == pos[3]:
                        continue
                    if (x, y, z, w) in cubes:
                        n += 1
                        if n > 3:
                            return n
    return n

def count_neighbors(pos, cubes):
    d = len(pos)
    if d == 3:
        return count_neighbors_3d(pos, cubes)
    elif d == 4:
        return count_neighbors_4d(pos, cubes)
    sys.exit(-1)

def simulate(cubes):
    new_cubes = set()
    for pos in positions(cubes):
        n = count_neighbors(pos, cubes)
        if pos in cubes:
            if n in (2, 3):
                new_cubes.add(pos)
        elif n == 3:
            new_cubes.add(pos)
    return new_cubes

def solve(cubes, dimensions, iterations):
    padding = [0] * (dimensions - 2)
    if padding:
        cubes = [tuple(list(cube) + padding) for cube in cubes]
    for _ in range(iterations):
        cubes = simulate(cubes)
    print(len(cubes))

cubes = set()
with open('../input/17.txt') as stream:
    for y, line in enumerate(stream):
        for x, c in enumerate(line):
            if c == '#':
                cubes.add((x, y))

solve(cubes, dimensions=3, iterations=6)
solve(cubes, dimensions=4, iterations=6)
