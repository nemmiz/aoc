#!/usr/bin/python3

def valid(a, b, c):
    if (a + b) <= c:
        return False
    if (a + c) <= b:
        return False
    if (b + c) <= a:
        return False
    return True

with open('../input/03.txt') as f:
    triangles = [tuple(map(int, line.split())) for line in f.readlines()]

vertical_triangles = []
for i in range(2, len(triangles), 3):
    vertical_triangles.append((triangles[i-2][0], triangles[i-1][0], triangles[i][0]))
    vertical_triangles.append((triangles[i-2][1], triangles[i-1][1], triangles[i][1]))
    vertical_triangles.append((triangles[i-2][2], triangles[i-1][2], triangles[i][2]))

print(sum((1 for a, b, c in triangles if valid(a, b, c))))
print(sum((1 for a, b, c in vertical_triangles if valid(a, b, c))))
