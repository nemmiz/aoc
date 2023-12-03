def find_subranges(numbers):
    """Find groups of number where the gap between them is <3"""
    numbers = sorted(numbers)
    subranges = []
    subrange = []
    for i in range(0, len(numbers)-1):
        if numbers[i+1] - numbers[i] < 3:
            subrange.append(numbers[i])
        else:
            if len(subrange) > 1:
                subrange.append(numbers[i])
                subranges.append(subrange)
            subrange = []
    if len(subrange) > 2:
        subranges.append(subrange)
    return subranges

def count_paths(lst):
    """Count possible paths through a subrange"""
    last_index = len(lst) - 1
    def _find_from(index):
        value = lst[index]
        found = 0
        for i in range(1, 4):
            next_index = index + i
            if next_index > last_index:
                continue
            next_value = lst[next_index]
            if next_value > (value + 3):
                continue
            if next_index == last_index:
                found += 1
            else:
                found += _find_from(next_index)
        return found
    return _find_from(0)

def part1(numbers):
    numbers = numbers.copy()
    jolts = 0
    diffs = {}
    while numbers:
        n = numbers.pop()
        diff = n - jolts
        diffs[diff] = diffs.get(diff, 0) + 1
        jolts = n
    print(diffs[1] * diffs[3])

def part2(numbers):
    result = 1
    for subrange in find_subranges(numbers):
        result *= count_paths(subrange)
    print(result)

with open('../input/10.txt') as stream:
    numbers = [int(line) for line in stream]

numbers.sort(reverse=True)
numbers.insert(0, numbers[0] + 3)
numbers.append(0)

part1(numbers)
part2(numbers)
