def part1(target):
    best = 0
    for vel in range(1, -target[2]):
        y = 0
        top = 0
        while True:
            y += vel
            top = max(y, top)
            vel -= 1
            if y < target[2]:
                break
            elif y <= target[3]:
                best = max(best, top)
                break
    print(best)
            
def part2(target):
    good = 0
    for yv in range(target[2], -target[2]):
        for xv in range(1, target[1]+1):
            pos = (0, 0)
            vel = (xv, yv)
            while True:
                pos = (pos[0]+vel[0], pos[1]+vel[1])
                vel = (max(0, vel[0]-1), vel[1]-1)
                if pos[0] > target[1] or pos[1] < target[2]:
                    break
                if (pos[0] >= target[0] and pos[0] <= target[1] and
                    pos[1] >= target[2] and pos[1] <= target[3]):
                    good += 1
                    break
    print(good)

with open('../input/17.txt') as stream:
    tmp = stream.read().split()
    a, b = tmp[2][2:-1].split('..')
    c, d = tmp[3][2:].split('..')
    target = (int(a), int(b), int(c), int(d))

part1(target)
part2(target)
