def decode(code):
    row, col = 0, 0
    for c in code:
        if c == 'F':
            row <<= 1
        elif c == 'B':
            row <<= 1
            row |= 1
        if c == 'L':
            col <<= 1
        elif c == 'R':
            col <<= 1
            col |= 1
    return row * 8 + col    

with open('../input/05.txt') as stream:
    seat_ids = [decode(line) for line in stream.readlines()]

seat_ids.sort()

print(seat_ids[-1])

first = seat_ids[0]
for i, sid in enumerate(seat_ids):
    if (sid - first) != i:
        print(sid - 1)
        break
