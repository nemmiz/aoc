from itertools import combinations

def exists_in_preamble(preamble, x):
    for a, b in combinations(preamble, 2):
        if a + b == x:
            return True
    return False

def find_invalid_number(numbers, preamble_size):
    for i in range(preamble_size, len(numbers)):
        if not exists_in_preamble(numbers[i-preamble_size:i], numbers[i]):
            return numbers[i]

def find_range_that_equals(numbers, x):
    a = 0
    b = 1
    while True:
        subrange = numbers[a:b]
        s = sum(subrange)
        if s == x:
            return min(subrange) + max(subrange)
        if s > x and a < b:
            a += 1
        else:
            b += 1

with open('../input/09.txt') as stream:
    numbers = [int(line) for line in stream]

x = find_invalid_number(numbers, 25)
print(x)
print(find_range_that_equals(numbers, x))
