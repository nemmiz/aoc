def cost_part1(positions, target, best):
    total_cost = 0
    for pos in positions:
        total_cost += abs(target - pos)
        if total_cost > best:
            break
    return total_cost

def cost_part2(positions, target, best):
    total_cost = 0
    for pos in positions:
        dist = abs(target - pos)
        total_cost += dist * (dist + 1) // 2
        if total_cost > best:
            break
    return total_cost

def solve(positions, cost_func):
    best = 10e10
    for pos in range(min(positions), max(positions)):
        best = min(best, cost_func(positions, pos, best))
    print(best)

with open('../input/07.txt') as stream:
    crabs = [int(x) for x in stream.read().split(',')]

solve(crabs, cost_part1)
solve(crabs, cost_part2)
