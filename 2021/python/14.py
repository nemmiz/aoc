def merge(c1, c2):
    return {k: c1.get(k, 0) + c2.get(k, 0) for k in set((*c1.keys(), *c2.keys()))}

def counts(pair, rules, remaining, cache):
    entry = (pair, remaining)
    if entry in cache:
        return cache[entry]

    e = rules[pair]
    if remaining == 1:
        if pair[0] == e:
            return {e: 2}
        return {e: 1, pair[0]: 1}

    result = merge(
        counts(f'{pair[0]}{e}', rules, remaining-1, cache),
        counts(f'{e}{pair[1]}', rules, remaining-1, cache),
    )

    cache[entry] = result
    return result

def solve(template, rules, steps):
    cache = {}
    result = {template[-1]: 1}
    for i in range(1, len(template)):
        result = merge(result, counts(template[i-1:i+1], rules, steps, cache))
    print(max(result.values()) - min(result.values()))

with open('../input/14.txt') as stream:
    lines = [line.strip() for line in stream.readlines()]
    template = lines[0]
    rules = dict([line.split(' -> ') for line in lines[2:]])

solve(template, rules, 10)
solve(template, rules, 40)
