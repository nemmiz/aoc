from functools import lru_cache

def deterministic_dice():
    while True:
        for i in range(1, 101):
            yield i

def part1(p1p, p2p):
    p1s, p2s = 0, 0
    dice = deterministic_dice()
    rolls = 0

    while True:
        moves = next(dice) + next(dice) + next(dice)
        rolls += 3
        p1p += moves
        while p1p > 10:
            p1p -= 10
        p1s += p1p
        if p1s >= 1000:
            print(rolls * p2s)
            break
        p1p, p1s, p2p, p2s = p2p, p2s, p1p, p1s

@lru_cache(maxsize=None)
def playrec(p1p, p2p, p1s, p2s, p1turn, universes):    
    w0 = check_score(p1p, p2p, p1s, p2s, p1turn, 3, universes)
    w1 = check_score(p1p, p2p, p1s, p2s, p1turn, 4, universes * 3)
    w2 = check_score(p1p, p2p, p1s, p2s, p1turn, 5, universes * 6)
    w3 = check_score(p1p, p2p, p1s, p2s, p1turn, 6, universes * 7)
    w4 = check_score(p1p, p2p, p1s, p2s, p1turn, 7, universes * 6)
    w5 = check_score(p1p, p2p, p1s, p2s, p1turn, 8, universes * 3)
    w6 = check_score(p1p, p2p, p1s, p2s, p1turn, 9, universes)
    p1wins = w0[0] + w1[0] + w2[0] + w3[0] + w4[0] + w5[0] + w6[0]
    p2wins = w0[1] + w1[1] + w2[1] + w3[1] + w4[1] + w5[1] + w6[1]
    return p1wins, p2wins

def check_score(p1p, p2p, p1s, p2s, p1turn, moves, universes):
    if p1turn:
        p1p += moves
        while p1p > 10:
            p1p -= 10
        p1s += p1p
        if p1s >= 21:
            return universes, 0
        return playrec(p1p, p2p, p1s, p2s, False, universes)
    else:
        p2p += moves
        while p2p > 10:
            p2p -= 10
        p2s += p2p
        if p2s >= 21:
            return 0, universes
        return playrec(p1p, p2p, p1s, p2s, True, universes)

def part2(p1pos, p2pos):
    print(max(playrec(p1pos, p2pos, 0, 0, True, 1)))    

with open('../input/21.txt') as stream:
    tmp = stream.read().split()
    p1pos = int(tmp[4])
    p2pos = int(tmp[9])

part1(p1pos, p2pos)
part2(p1pos, p2pos)
