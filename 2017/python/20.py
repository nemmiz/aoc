#!/usr/bin/python3

from itertools import count


def part1(particles):
    accels = []
    for p in particles:
        accels.append(abs(p[6])+abs(p[7])+abs(p[8]))
    print(accels.index(min(accels)))


def part2(particles):
    particles = {i: p for i, p in enumerate(particles)}
    last_collision = 0
    for steps in count():
        poscount = {}
        for i, p in particles.items():
            pos = tuple(p[0:3])
            if pos in poscount:
                poscount[pos].append(i)
            else:
                poscount[pos] = [i]
        
        if len(particles) != len(poscount):
            to_remove = []
            for pos, ps in poscount.items():
                if len(ps) > 1:
                    to_remove.extend(ps)
            for i in to_remove:
                del particles[i]
            last_collision = steps

        if steps > (last_collision + 100):
            print(len(particles))
            break
        
        for i, p in particles.items():
            p[3] += p[6]
            p[4] += p[7]
            p[5] += p[8]
            p[0] += p[3]
            p[1] += p[4]
            p[2] += p[5]


with open('../input/20.txt') as f:
    particles = []
    pattern = '(?!-)(-?\d+)'.join(['.*']*10)
    for line in f.readlines():
        line = line.replace('p=<', '')
        line = line.replace('v=<', '')
        line = line.replace('a=<', '')
        line = line.replace('>', '')
        particles.append([int(n) for n in line.split(',')])

part1(particles)
part2(particles)
