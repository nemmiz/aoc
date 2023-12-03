def simulate(fish, iterations):
    fishes = [0] * 9
    for f in fish:
        fishes[f] += 1
    for _ in range(iterations):
        zeros = fishes[0]
        for i in range(8):
            fishes[i] = fishes[i+1]
        fishes[8] = zeros
        fishes[6] += zeros
    print(sum(fishes))

with open('../input/06.txt') as stream:
    fish = [int(x) for x in stream.read().split(',')]

simulate(fish, 80)
simulate(fish, 256)
