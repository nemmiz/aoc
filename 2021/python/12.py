def part1(connections):
    finished_paths = 0
    paths = ['start']
    while paths:
        path = paths.pop()
        steps = path.split(',')
        visited = [step for step in steps if step.islower()]
        current = steps[-1]

        if current == 'end':
            finished_paths += 1
            continue

        for connection in connections[current]:
            if connection not in visited:
                paths.append(f'{path},{connection}')

    print(finished_paths)


def part2(connections):
    finished_paths = 0
    paths = [('start', set(), False)]
    while paths:
        path, visited, visited_twice = paths.pop()
        current = path[path.rfind(',')+1:]

        if current == 'end':
            finished_paths += 1
            continue

        for connection in connections[current]:
            if connection == 'start':
                continue
            elif connection.isupper():
                paths.append((f'{path},{connection}', visited, visited_twice))
            elif connection not in visited:
                paths.append((f'{path},{connection}', {*visited, connection}, visited_twice))
            elif not visited_twice:
                paths.append((f'{path},{connection}', visited, True))

    print(finished_paths)


with open('../input/12.txt') as stream:
    connections = {}
    for line in stream.readlines():
        src, dst = line.strip().split('-')
        connections[src] = [*connections.get(src,[]), dst]
        connections[dst] = [*connections.get(dst,[]), src] 

part1(connections)
part2(connections)
