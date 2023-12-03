#!/usr/bin/python3

def escape_string(s):
    replace = {'"': '\\"', '\\': '\\\\'}
    return '"'+''.join([replace.get(c, c) for c in s])+'"'

with open('../input/08.txt') as f:
    lines = [line.strip() for line in f.readlines()]

print(sum((len(line) - len(eval(line)) for line in lines)))
print(sum((len(escape_string(line)) - len(line) for line in lines)))
