def modinv(a, b):
    return pow(a, -1, b)

def chinese_remainder_theorem(m, x):
    while len(x) > 1:
        temp1 = modinv(m[1], m[0]) * x[0] * m[1] + modinv(m[0], m[1]) * x[1] * m[0]
        temp2 = m[0] * m[1]
        x = [temp1 % temp2] + x[2:]
        m = [temp2] + m[2:]
    return x[0]

def part1(lines):
    earliest = int(lines[0])
    buses = [int(bus) for bus in lines[1].split(',') if bus != 'x']
    departures = [(earliest + bus - 1) // bus * bus for bus in buses]
    best = min(departures)
    best_bus = buses[departures.index(best)]
    print((best - earliest) * best_bus)

def part2(lines):
    buses, times = [], []
    for i, bus in enumerate(lines[1].split(',')):
        if bus != 'x':
            buses.append(int(bus))
            times.append(-i)
    print(chinese_remainder_theorem(buses, times))

with open('../input/13.txt') as stream:
    lines = [line.strip() for line in stream]

part1(lines)
part2(lines)
