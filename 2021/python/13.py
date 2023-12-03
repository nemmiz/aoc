def fold(points, instruction):
    axis, pos = instruction
    new_points = set()
    for x, y in points:
        if y > pos and axis == 'y':
            y = pos - (y - pos)
        if x > pos and axis == 'x':
            x = pos - (x - pos)
        new_points.add((x, y))
    return new_points

def display(points):
    max_pos = max(points)
    for y in range(max_pos[1]+1):
        for x in range(max_pos[0]+1):
            print('#' if (x, y) in points else ' ', end='')
        print()

with open('../input/13.txt') as stream:
    points = set()
    folds = []

    for line in stream.readlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith('fold'):
            folds.append((line[11], int(line[13:])))
        else:
            x, y = line.split(',')
            points.add((int(x), int(y)))

# Part 1
print(len(fold(points, folds[0])))

# Part 2
for instruction in folds:
    points = fold(points, instruction)
display(points)