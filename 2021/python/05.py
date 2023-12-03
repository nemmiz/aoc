
def solve(segs, do_diagonals):
    points = {}

    for x1, y1, x2, y2 in segs:
        if x1 != x2 and y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                point = (x, y1)
                points[point] = points.get(point, 0) + 1
        elif y1 != y2 and x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                point = (x1, y)
                points[point] = points.get(point, 0) + 1
        elif do_diagonals and abs(x1-x2) == abs(y1-y2):
            dx = 1 if x2 > x1 else -1
            dy = 1 if y2 > y1 else -1
            point = (x1, y1)
            while point != (x2+dx, y2+dy):
                points[point] = points.get(point, 0) + 1
                point = (point[0]+dx, point[1]+dy)
    
    print(sum(1 for overlaps in points.values() if overlaps >= 2))


segments = []
with open('../input/05.txt') as stream:
    for line in stream.readlines():
        a, b, c, d = line.replace(' -> ', ',').split(',')
        segments.append((int(a), int(b), int(c), int(d)))

solve(segments, do_diagonals=False)
solve(segments, do_diagonals=True)
