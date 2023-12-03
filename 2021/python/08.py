def decode(line):
    tmp = line.replace(' | ', ' ').split()
    patterns = tmp[:-4]
    outputs = tmp[-4:]

    segmap = {}
    for pat in patterns:
        segmap[len(pat)] = segmap.get(len(pat), set()) | set(pat)

    notin609 = set()
    for pat in patterns:
        if len(pat) == 6:
            notin609.update(segmap[7] - set(pat))

    notin235 = set()
    for pat in patterns:
        if len(pat) == 5:
            notin235.update(segmap[7] - set(pat))

    possible = {}
    possible[0] = segmap[3] - segmap[2]
    possible[1] = (segmap[4] - segmap[2]) & notin235
    possible[2] = segmap[2]
    possible[3] = segmap[4] - segmap[2] & notin609
    possible[4] = (notin609 - segmap[4] - segmap[2]) & notin235
    possible[5] = (segmap[2] - notin609) & notin235
    possible[6] = segmap[7] - segmap[4] - segmap[3] - notin609 - notin235

    solved = set()
    while len(solved) != 7:
        for i, p in possible.items():
            if len(p) == 1:
                solved.update(p)
            elif len(p) > 1:
                possible[i] -= solved

    seg2bit = {list(p)[0]: 6-i for i, p in possible.items()}

    segbits2num = {
        0b1110111: 0,
        0b0010010: 1,
        0b1011101: 2,
        0b1011011: 3,
        0b0111010: 4,
        0b1101011: 5,
        0b1101111: 6,
        0b1010010: 7,
        0b1111111: 8,
        0b1111011: 9,
    }

    number = 0
    for output in outputs:
        segbits = 0
        for char in output:
            segbits |= (1 << seg2bit[char])
        number = number * 10 + segbits2num[segbits]
    return number


with open('../input/08.txt') as stream:
    part1sum = 0
    part2sum = 0
    for line in stream.readlines():
        part2sum += decode(line)
        _, tmp = line.split(' | ')
        for s in tmp.split():
            if len(s) in (2, 3, 4, 7):
                part1sum += 1
    print(part1sum)
    print(part2sum)
