from heapq import heappush, heappop

def find_lowest_risk(risk_levels):
    end = max(risk_levels.keys())
    paths = [(0, (0, 0))]
    visited = {(0, 0): 1}
    while paths:
        cost, last = heappop(paths)
        if last == end:
            return cost
        if last in visited and cost >= visited[last]:
            continue
        visited[last] = cost
        for adj in ((last[0], last[1]+1), (last[0]+1, last[1]), 
                    (last[0]-1, last[1]), (last[0], last[1]-1)):
            if adj in risk_levels:
                heappush(paths, (cost+risk_levels[adj], adj))
    

def expand(risk_levels):
    expanded = {}
    maxx, maxy = max(risk_levels.keys())
    for point, risk in risk_levels.items():
        for x in range(5):
            for y in range(5):
                new_point = ((maxx+1) * x + point[0], (maxy+1) * y + point[1])
                new_risk = risk + x + y
                if new_risk > 9:
                    new_risk -= 9
                expanded[new_point] = new_risk
    return expanded

with open('../input/15.txt') as stream:
    risk_levels = {}
    for y, line in enumerate(stream.readlines()):
        for x, c in enumerate(line.strip()):
            risk_levels[(x, y)] = int(c)

print(find_lowest_risk(risk_levels))
print(find_lowest_risk(expand(risk_levels)))
