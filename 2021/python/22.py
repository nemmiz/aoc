from collections import namedtuple

Cube = namedtuple('Cube', 'minx miny minz maxx maxy maxz')

def valid(cube):
    return (cube.maxx-cube.minx) >= 0 and (cube.maxy-cube.miny) >= 0 and (cube.maxz-cube.minz) >= 0

def size(cube):
    return (cube.maxx+1-cube.minx) * (cube.maxy+1-cube.miny) * (cube.maxz+1-cube.minz)

def subtract(a, b):
    xs = ((a.minx, b.minx-1), (max(a.minx, b.minx), min(a.maxx, b.maxx)), (b.maxx+1, a.maxx))
    ys = ((a.miny, b.miny-1), (max(a.miny, b.miny), min(a.maxy, b.maxy)), (b.maxy+1, a.maxy))
    zs = ((a.minz, b.minz-1), (max(a.minz, b.minz), min(a.maxz, b.maxz)), (b.maxz+1, a.maxz))
    new_cubes = []
    for xi in range(3):
        for yi in range(3):
            for zi in range(3):
                if xi == 1 and yi == 1 and zi == 1:
                    continue
                cube = Cube(xs[xi][0], ys[yi][0], zs[zi][0], xs[xi][1], ys[yi][1], zs[zi][1])
                if valid(cube):
                    new_cubes.append(cube)
    return new_cubes

def intersection(a, b):
    if a.minx > b.maxx or a.maxx < b.minx:
        return None
    if a.miny > b.maxy or a.maxy < b.miny:
        return None
    if a.minz > b.maxz or a.maxz < b.minz:
        return None
    return Cube(
        minx=max(a.minx, b.minx),
        miny=max(a.miny, b.miny),
        minz=max(a.minz, b.minz),
        maxx=min(a.maxx, b.maxx),
        maxy=min(a.maxy, b.maxy),
        maxz=min(a.maxz, b.maxz),
    )

def solve(instructions):
    cubes = []
    for step, x0, x1, y0, y1, z0, z1 in instructions:
        if step == 'on':
            new_cubes = [Cube(x0, y0, z0, x1, y1, z1)]
            while new_cubes:
                new_cube = new_cubes.pop()    
                for cube in cubes:
                    if (tmp := intersection(cube, new_cube)) is not None:
                        new_cubes.extend(subtract(new_cube, tmp))
                        break
                else:
                    cubes.append(new_cube)
        if step == 'off':
            subcube = Cube(x0, y0, z0, x1, y1, z1)
            new_cubes = []
            for cube in cubes:
                if (intr := intersection(cube, subcube)) is None:
                    new_cubes.append(cube)
                else:
                    new_cubes.extend(subtract(cube, subcube))
            cubes = new_cubes

    print(sum(size(cube) for cube in cubes))

def clip_instructions(instructions, minx, miny, minz, maxx, maxy, maxz):
    clipped = []
    for step, x0, x1, y0, y1, z0, z1 in instructions:
        x0 = max(x0, minx)
        y0 = max(y0, miny)
        z0 = max(z0, minz)
        x1 = min(x1, maxx)
        y1 = min(y1, maxy)
        z1 = min(z1, maxz)
        if x0 <= x1 and y0 <= y1 and z0 <= z1:
            clipped.append((step, x0, x1, y0, y1, z0, z1))
    return clipped

with open('../input/22.txt') as stream:
    instructions = []
    for line in stream.readlines():
        tmp = line.replace(',', ' ').split()
        inst = [tmp[0]]
        inst.extend([int(x) for x in tmp[1][2:].split('..')])
        inst.extend([int(x) for x in tmp[2][2:].split('..')])
        inst.extend([int(x) for x in tmp[3][2:].split('..')])
        instructions.append(inst)

clipped = clip_instructions(instructions, -50, -50, -50, 50, 50, 50)
solve(clipped)
solve(instructions)
