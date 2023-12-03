from operator import mul
from functools import reduce

with open('../input/03.txt') as stream:
    map_data = [line.strip() for line in stream]

map_width = len(map_data[0])
map_height = len(map_data)

def check_slope(x, y):
    pos = (0, 0)
    trees = 0
    while True:
        pos = (pos[0]+x, pos[1]+y)
        if pos[1] >= map_height:
            break
        if map_data[pos[1]][pos[0]%map_width] == '#':
            trees += 1
    return trees

answers = [check_slope(x, y) for x, y in [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]]

print(answers[1])
print(reduce(mul, answers, 1))
