#!/usr/bin/python3

import hashlib
import itertools

def calculate_hash(n, salt, stretch):
    h = hashlib.md5((salt + str(n)).encode('ascii')).hexdigest()
    if stretch:
        for i in range(2016):
            h = hashlib.md5(h.encode('ascii')).hexdigest()
    return h

def calculate_keys(salt, stretch):
    cache = {}
    found_quints = 0

    for i in itertools.count():
        if i not in cache:
            cache[i] = calculate_hash(i, salt, stretch)
        result = cache[i]

        for k in range(2, len(result)):
            if result[k] == result[k-1] and result[k] == result[k-2]:
                quint = result[k] * 5
                for j in range(i+1, i+1001):
                    if j not in cache:
                        cache[j] = calculate_hash(j, salt, stretch)
                    if quint in cache[j]:
                        print('.', end='', flush=True)
                        found_quints += 1
                        break
                break

        if found_quints == 64:
            print()
            return i

print(calculate_keys('zpqevtbw', stretch=False))
print(calculate_keys('zpqevtbw', stretch=True))
