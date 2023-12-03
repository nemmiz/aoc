#!/usr/bin/python3


def knot_hash(puzzle_input):
    lengths = [ord(c) for c in puzzle_input] + [17, 31, 73, 47, 23]
    pos, skip = 0, 0
    sparse = list(range(256))
    for _ in range(64):
        for length in lengths:
            i = pos
            tmp = []
            while len(tmp) != length:
                tmp.append(sparse[i%len(sparse)])
                i += 1
            tmp.reverse()
            i = pos
            for x in tmp:
                sparse[i%len(sparse)] = x
                i += 1
            pos = (pos + length + skip) % len(sparse)
            skip += 1
    dense = []
    for i in range(0, len(sparse), 16):
        tmp = sparse[i]
        for j in range(i+1, i+16):
            tmp ^= sparse[j]
        dense.append(tmp)
    return ''.join(['{0:02x}'.format(x) for x in dense])


def hex2bin(h):
    lookup = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'a': '1010', 'b': '1011',
        'c': '1100', 'd': '1101', 'e': '1110', 'f': '1111',
    }
    return ''.join([lookup[c] for c in h])


def make_grid(key):
    return [hex2bin(knot_hash(key+'-'+str(i))) for i in range(128)]


def remove_region(points, origin):
    x, y = origin
    neighbors = [
        (x, y-1),
        (x, y+1),
        (x-1, y),
        (x+1, y),
    ]
    for point in neighbors:
        if point in points:
            points.remove(point)
            remove_region(points, point)


def part1(grid):
    print(sum(row.count('1') for row in grid))


def part2(grid):
    points = set()
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == '1':
                points.add((x, y))
    regions = 0
    while points:
        regions += 1
        point = points.pop()
        remove_region(points, point)
    print(regions)


grid = make_grid('ugkiagan')
part1(grid)
part2(grid)
