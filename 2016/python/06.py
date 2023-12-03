#!/usr/bin/python3

with open('../input/06.txt') as f:
    messages = [line.strip() for line in f.readlines()]

cols = len(messages[0])
message1 = ['_'] * cols
message2 = ['_'] * cols

for i in range(cols):
    occurances = {}
    for message in messages:
        c = message[i]
        occurances[c] = occurances.get(c, 0) + 1
    most = max(occurances.values())
    least = min(occurances.values())
    for c, o in occurances.items():
        if o == most:
            message1[i] = c
        if o == least:
            message2[i] = c

print(''.join(message1))
print(''.join(message2))
