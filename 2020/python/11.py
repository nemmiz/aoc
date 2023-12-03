def calculate_adjacent(positions):
    offsets = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
    adjacency = []
    pos_map = {pos: i for i, pos in enumerate(positions)}
    for pos in positions:
        adjacent = []
        for offset in offsets:
            tmp = (pos[0] + offset[0], pos[1] + offset[1])
            if tmp in pos_map:
                adjacent.append(pos_map[tmp])
        adjacency.append(adjacent)
    return adjacency

def calculate_visible(positions):
    max_pos = max(positions)
    deltas = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
    visibility = []
    pos_map = {pos: i for i, pos in enumerate(positions)}
    for pos in positions:
        visible = []
        for delta in deltas:
            tmp = pos
            while True:
                tmp = (tmp[0] + delta[0], tmp[1] + delta[1])
                if tmp in pos_map:
                    visible.append(pos_map[tmp])
                    break
                if tmp[0] < 0 or tmp[1] < 0 or tmp[0] > max_pos[0] or tmp[1] > max_pos[1]:
                    break
        visibility.append(visible)
    return visibility

def simulate(grid, visibility, tolerance):
    new_grid = []
    for value, vis in zip(grid, visibility):
        n = 0
        for v in vis:
            n += grid[v]
        if value == 0 and n == 0:
            new_grid.append(1)
        elif value == 1 and n >= tolerance:
            new_grid.append(0)
        else:
            new_grid.append(value)
    return new_grid

def simulate_until_stable(grid, visibility, tolerance):
    while (new_grid := simulate(grid, visibility, tolerance)) != grid:
        grid = new_grid
    return sum(grid)

grid = []
positions = []
with open('../input/11.txt') as stream:
    for y, line in enumerate(stream):
        for x, c in enumerate(line):
            if c == 'L':
                positions.append((x, y))
                grid.append(0)

print(simulate_until_stable(grid, calculate_adjacent(positions), 4))
print(simulate_until_stable(grid, calculate_visible(positions), 5))
