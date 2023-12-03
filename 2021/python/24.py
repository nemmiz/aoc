with open('../input/24.txt') as stream:
    constants = []
    lines = stream.readlines()
    for i in range(0, len(lines), 18):
        c0 = int(lines[i+5].split()[-1])
        c1 = int(lines[i+15].split()[-1])
        constants.append((c0, c1))

min_num = [None] * 14
max_num = [None] * 14
stack = []

for i, c in enumerate(constants):
    if c[0] > 0:
        stack.append((c[1], i))
    elif c[0] < 0:
        x, xi = stack.pop()
        d = x + c[0]
        if d <= 0:
            min_num[xi] = 1 - d
            min_num[i] = 1
            max_num[xi] = 9
            max_num[i] = 9 + d
        else:
            min_num[xi] = 1
            min_num[i] = 1 + d
            max_num[xi] = 9 - d
            max_num[i] = 9

print(''.join(str(i) for i in max_num))
print(''.join(str(i) for i in min_num))
