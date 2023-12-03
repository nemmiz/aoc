#!/usr/bin/python3

import json
from itertools import repeat

def check(data, skip_red):
    if isinstance(data, int):
        return data
    elif isinstance(data, list):
        return sum(map(check, data, repeat(skip_red)))
    elif isinstance(data, dict):
        if skip_red and 'red' in data.values():
            return 0
        return sum(map(check, data.values(), repeat(skip_red)))
    return 0

with open('../input/12.txt') as f:
    data = json.load(f)

print(check(data, skip_red=False))
print(check(data, skip_red=True))
