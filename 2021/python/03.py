def part1(numbers):
    maxlen = max(len(x) for x in numbers)
    most_common = []
    least_common = []

    for i in range(maxlen):
        ones, zeros = 0, 0
        for d in data:
            if d[i] == '1':
                ones += 1
            elif d[i] == '0':
                zeros += 1
        if ones > zeros:
            most_common.append('1')
            least_common.append('0')
        else:
            most_common.append('0')
            least_common.append('1')

    print(int(''.join(most_common), 2) * int(''.join(least_common), 2))


def find_rating(numbers, pos, find_most_common):
    if len(numbers) == 1:
        return int(numbers[0], 2)

    nums_with_0 = []
    nums_with_1 = []
    for number in numbers:
        if number[pos] == '0':
            nums_with_0.append(number)
        elif number[pos] == '1':
            nums_with_1.append(number)

    if find_most_common:
        if len(nums_with_0) == len(nums_with_1):
            return find_rating(nums_with_1, pos+1, find_most_common)
        if len(nums_with_0) > len(nums_with_1):
            return find_rating(nums_with_0, pos+1, find_most_common)
        if len(nums_with_0) < len(nums_with_1):
            return find_rating(nums_with_1, pos+1, find_most_common)
    else:
        if len(nums_with_0) == len(nums_with_1):
            return find_rating(nums_with_0, pos+1, find_most_common)
        if len(nums_with_0) > len(nums_with_1):
            return find_rating(nums_with_1, pos+1, find_most_common)
        if len(nums_with_0) < len(nums_with_1):
            return find_rating(nums_with_0, pos+1, find_most_common)


def part2(numbers):
    print(find_rating(data, 0, True) * find_rating(data, 0, False))


with open('../input/03.txt') as stream:
    data = [line.strip() for line in stream.readlines()]

part1(data)
part2(data)
