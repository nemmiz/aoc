#!/usr/bin/python3

def move_iter(speed, flight_time, rest_time):
    distance = 0
    while True:
        for _ in range(flight_time):
            distance += speed
            yield distance
        for _ in range(rest_time):
            yield distance

reindeer = {}
with open('../input/14.txt') as f:
    for line in f.readlines():
        parts = line.split()
        it = move_iter(int(parts[3]), int(parts[6]), int(parts[13]))
        reindeer[parts[0]] = [next(it) for _ in range(2503)]

print(max((distances[-1] for distances in reindeer.values())))

scores = {name: 0 for name in reindeer.keys()}
for i in range(2503):
    best = max((distances[i] for distances in reindeer.values()))
    for name, distances in reindeer.items():
        if distances[i] == best:
            scores[name] += 1

print(max(scores.values()))
