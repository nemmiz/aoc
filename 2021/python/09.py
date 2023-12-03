def adjacent(point):
    yield (point[0]-1, point[1])
    yield (point[0]+1, point[1])
    yield (point[0], point[1]-1)
    yield (point[0], point[1]+1)

def find_low_points(heights):
    low_points = []
    for point, value in heights.items():
        if all(value < heights.get(adj, 9) for adj in adjacent(point)):
            low_points.append(point)
    return low_points

def basin_size(point, heights):
    checked_points = set()
    points_to_check = [point]
    size = 0
    while points_to_check:
        p = points_to_check.pop()
        if p in checked_points:
            continue
        checked_points.add(p)
        if heights.get(p, 9) < 9:
            size += 1
            for adj in adjacent(p):
                if adj not in checked_points:
                    points_to_check.append(adj)
    return size

with open('../input/09.txt') as stream:
    heights = {}
    for y, line in enumerate(stream.readlines()):
        for x, c in enumerate(line.strip()):
            heights[(x, y)] = int(c)

# Part 1
low_points = find_low_points(heights)
print(sum(heights[p]+1 for p in low_points))

# Part 2
basin_sizes = [basin_size(low, heights) for low in low_points]
basin_sizes.sort()
print(basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3])
    