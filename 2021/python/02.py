def part1(commands):
    position = 0
    depth = 0

    for command, amount in commands:
        if command == 'forward':
            position += amount
        elif command == 'up':
            depth -= amount
        elif command == 'down':
            depth += amount

    print(position * depth)


def part2(commands):
    aim = 0
    position = 0
    depth = 0

    for command, amount in commands:
        if command == 'forward':
            position += amount
            depth += aim * amount
        elif command == 'up':
            aim -= amount
        elif command == 'down':
            aim += amount

    print(position * depth)


commands = []
with open('../input/02.txt') as stream:
    for line in stream.readlines():
        cmd, amt = line.split()
        commands.append((cmd, int(amt)))

part1(commands)
part2(commands)
