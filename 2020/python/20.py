import sys
from copy import deepcopy
from math import sqrt

def rotate(img):
    size = len(img)
    return [
        ''.join([img[j][i] for j in range(size-1, -1, -1)])
        for i in range(size)
    ]

def rotate2(img):
    return [line[::-1] for line in reversed(img)]

def rotate3(img):
    size = len(img)
    return [
        ''.join([line[i] for line in img])
        for i in range(size-1, -1, -1)
    ]

def flip_h(img):
    return [line[::-1] for line in img]

def flip_v(img):
    return img[::-1]

def variations(tile):
    yield tile
    yield flip_h(tile)
    yield flip_v(tile)
    yield rotate(tile)
    yield rotate2(tile)
    yield rotate3(tile)
    yield flip_h(rotate(tile))
    yield flip_v(rotate(tile))

def top(tile):
    return tile[0]

def bottom(tile):
    return tile[-1]

def left(tile):
    return ''.join([tile[i][0] for i in range(len(tile))])

def right(tile):
    return ''.join([tile[i][-1] for i in range(len(tile))])

def get_edges(tile):
    return (top(tile), bottom(tile), left(tile), right(tile))

def compute_edge_cache(tiles):
    cache = {}
    for tid, tile in tiles.items():
        edges = [top(tile), bottom(tile), left(tile), right(tile)]
        for edge in edges:
            s = cache.get(edge, set())
            s.add(tid)
            cache[edge] = s
            rev = edge[::-1]
            s = cache.get(rev, set())
            s.add(tid)
            cache[rev] = s
    return cache

def edge_tile_count(cache, edge, ignore=None):
    s = cache[edge]
    if ignore in s:
        return len(s) - 1
    return len(s)

def get_image(grid, size):
    dim = size * 8
    img = []
    for y in range(dim):
        line = []
        for x in range(dim):
            tx = x // 8
            ty = y // 8
            line.append(grid[(tx, ty)][((y % 8) + 1)][(x % 8) + 1])
        img.append(''.join(line))
    return img

def count_and_mark_monsters(img):
    monster = [
        '                  # ',
        '#    ##    ##    ###',
        ' #  #  #  #  #  #   '
    ]

    offsets = []
    for y, line in enumerate(monster):
        for x, c in enumerate(line):
            if c == '#':
                offsets.append((x, y))

    monster_height = len(monster)
    monster_width = len(monster[0])
    monsters_found = 0

    for y in range(len(img)-monster_height):
        for x in range(len(img[0])-monster_width):
            for offset in offsets:
                xx = x + offset[0]
                yy = y + offset[1]
                if img[yy][xx] != '#':
                    break
            else:
                monsters_found += 1
                for offset in offsets:
                    xx = x + offset[0]
                    yy = y + offset[1]
                    tmp = list(img[yy])
                    tmp[xx] = 'O'
                    img[yy] = ''.join(tmp)

    return monsters_found

def calculate_roughness(img):
    for variation in variations(img):
        if count_and_mark_monsters(variation) != 0:
            break
    return sum(line.count('#') for line in variation)

def part1(tiles, cache):
    result = 1
    for tid, tile in tiles.items():
        n = 0
        for edge in get_edges(tile):
            if edge_tile_count(cache, edge, ignore=tid):
                n += 1
        if n == 2:
            result *= tid
    print(result)

def part2(tiles, cache):
    grid = {}
    size = int(sqrt(len(tiles)))
    tiles = deepcopy(tiles)
    for tid, tile in tiles.items():
        m = [edge_tile_count(cache, e, ignore=tid) for e in get_edges(tile)]
        if m == [0, 1, 0, 1]:
            break
    del tiles[tid]
    grid[(0, 0)] = tile
    for y in range(size):
        for x in range(size):
            pos = (x, y)
            if x == 0:
                if y == 0:
                    continue
                requirement = bottom(grid[(x, y-1)])
                check_dir = top
            else:
                requirement = right(grid[(x-1, y)])
                check_dir = left
            for tid, tile in tiles.items():
                for v in variations(tile):
                    if check_dir(v) == requirement:
                        grid[pos] = v
                        del tiles[tid]
                        break
                else:
                    continue
                break
    print(calculate_roughness(get_image(grid, size)))

tiles = {}
with open('../input/20.txt') as stream:
    for chunk in stream.read().split('\n\n'):
        lines = chunk.split('\n')
        _, tid = lines[0].split()
        tid = int(tid[:-1])
        tiles[tid] = lines[1:]

cache = compute_edge_cache(tiles)
part1(tiles, cache)
part2(tiles, cache)
