from itertools import combinations

with open('../input/01.txt') as stream:
    numbers = [int(line) for line in stream]

for a, b in combinations(numbers, 2):
    if (a + b) == 2020:
        print(a * b)

for a, b, c in combinations(numbers, 3):
    if (a + b + c) == 2020:
        print(a * b * c)
