#!/usr/bin/python3

from itertools import count
from io import StringIO

def generate_data(initial, size):
    while len(initial) < size:
        initial = initial + '0' + ''.join(['0' if c == '1' else '1' for c in reversed(initial)])
    return initial[:size]

def calculate_checksum(data):
    while len(data) % 2 == 0:
        new_data = StringIO()
        for i in range(1, len(data), 2):
            if data[i] == data[i-1]:
                new_data.write('1')
            else:
                new_data.write('0')
        data = new_data.getvalue()
    return data

print(calculate_checksum(generate_data('10111011111001111', 272)))
print(calculate_checksum(generate_data('10111011111001111', 35651584)))
