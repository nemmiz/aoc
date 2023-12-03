from itertools import combinations

def rx(point):
    return (point[0], -point[2], point[1])

def ry(point):
    return (point[2], point[1], -point[0])

def orientations(beacons):
    yield beacons
    yield [ry(b) for b in beacons]
    yield [ry(ry(b)) for b in beacons]
    yield [ry(ry(ry(b))) for b in beacons]

    yield [rx(b) for b in beacons]
    yield [rx(ry(b)) for b in beacons]
    yield [rx(ry(ry(b))) for b in beacons]
    yield [rx(ry(ry(ry(b)))) for b in beacons]

    yield [rx(rx(b)) for b in beacons]
    yield [rx(rx(ry(b))) for b in beacons]
    yield [rx(rx(ry(ry(b)))) for b in beacons]
    yield [rx(rx(ry(ry(ry(b))))) for b in beacons]

    yield [rx(rx(rx(b))) for b in beacons]
    yield [rx(rx(rx(ry(b)))) for b in beacons]
    yield [rx(rx(rx(ry(ry(b))))) for b in beacons]
    yield [rx(rx(rx(ry(ry(ry(b)))))) for b in beacons]

    yield [ry(rx(b)) for b in beacons]
    yield [ry(rx(ry(b))) for b in beacons]
    yield [ry(rx(ry(ry(b)))) for b in beacons]
    yield [ry(rx(ry(ry(ry(b))))) for b in beacons]

    yield [ry(ry(ry(rx(b)))) for b in beacons]
    yield [ry(ry(ry(rx(ry(b))))) for b in beacons]
    yield [ry(ry(ry(rx(ry(ry(b)))))) for b in beacons]
    yield [ry(ry(ry(rx(ry(ry(ry(b))))))) for b in beacons]

def largest_manhattan(positions):
    result = 0
    for a, b in combinations(positions, 2):
        result = max(result, abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]))
    return result

def match_scanners(a, b):
    for ba in a:
        for ori in orientations(b):
            for bb in ori:
                dx = ba[0] - bb[0]
                dy = ba[1] - bb[1]
                dz = ba[2] - bb[2]
                tmp = {(beacon[0]+dx, beacon[1]+dy, beacon[2]+dz) for beacon in ori}
                if len(a & tmp) >= 12:
                    return a | tmp, (dx, dy, dz)
    return None

def solve(scanners):
    full_map = scanners[0].copy()
    todo = scanners[1:]
    scanner_positions = []
    while todo:
        scanner = todo[0]
        todo = todo[1:]
        tmp = match_scanners(full_map, scanner)
        if tmp:
            full_map = tmp[0]
            scanner_positions.append(tmp[1])
        else:
            todo.append(scanner)
    print(len(full_map))
    print(largest_manhattan(scanner_positions))

with open('../input/19.txt') as stream:
    scanners = []
    current = None

    for line in stream.readlines():
        line = line.strip()
        if line.startswith('---'):
            current = set()
            scanners.append(current)
        elif not line:
            continue
        else:
            a, b, c = line.split(',')
            current.add((int(a), int(b), int(c)))

solve(scanners)
