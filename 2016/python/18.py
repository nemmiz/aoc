#!/usr/bin/python3

def next_row(row, rules):
    n = len(row)
    new_row = []
    for i in range(n):
        left = False if i == 0 else row[i-1] == '^'
        center = row[i] == '^'
        right = False if i == (n-1) else row[i+1] == '^'
        if left and center and not right:
           new_row.append('^')
        elif center and right and not left:
           new_row.append('^')
        elif left and not center and not right:
           new_row.append('^')
        elif right and not center and not left:
           new_row.append('^')
        else:
           new_row.append('.')
    return ''.join(new_row)

def count_safe_tiles(row, n):
    rules = (0, 1, 0, 1, 1, 0, 1, 0)
    rows = [row]
    for _ in range(n-1):
        row = next_row(row, rules)
        rows.append(row)
    return sum((r.count('.') for r in rows))

with open('../input/18.txt') as f:
    row = f.read()

print(count_safe_tiles(row, 40))
print(count_safe_tiles(row, 400000))
