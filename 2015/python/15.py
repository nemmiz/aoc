#!/usr/bin/python3

def spliterator(n, amount):
    lst = [0 for _ in range(n)]
    lst[-1] = amount

    yield tuple(lst)

    while True:
        for i in range(n-2, -1, -1):
            lst[i] += 1
            rem = amount - sum(lst[:-1])
            if rem < 0:
                lst[i] = 0
            else:
                lst[-1] = rem
                yield tuple(lst)
                break
        else:
            break
    
ingredients = []
with open('../input/15.txt') as f:
    for line in f.readlines():
        parts = line.split()
        ingredients.append(tuple(int(parts[i].rstrip(',')) for i in range(2, len(parts), 2)))

best = 0
best500 = 0

for amounts in spliterator(len(ingredients), 100):
    props = [0, 0, 0, 0, 0]
    for ingredient, amount in zip(ingredients, amounts):
        for i in range(len(props)):
            props[i] += ingredient[i] * amount

    total = 1
    for prop in props[:-1]:
        total *= max(0, prop)

    best = max(best, total)

    if props[-1] == 500:
        best500 = max(best500, total)

print(best)
print(best500)
