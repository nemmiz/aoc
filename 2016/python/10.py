#!/usr/bin/python3

from collections import deque

with open('../input/10.txt') as f:
    instructions = deque([line.split() for line in f.readlines()])

bots = {}
outputs = {}

while instructions:
    inst = instructions.popleft()

    if inst[0] == 'value':
        val = int(inst[1])
        bot = int(inst[5])
        bots[bot] = bots.get(bot, [])
        bots[bot].append(val)
    elif inst[0] == 'bot':
        sender_id = int(inst[1])
        sender_values = bots.get(sender_id, [])
        if len(sender_values) != 2:
            instructions.append(inst)
            continue
        lo = min(sender_values)
        hi = max(sender_values)
        if lo == 17 and hi == 61:
            print(sender_id)
        assert(inst[3] == 'low')
        assert(inst[8] == 'high')
        if inst[5] == 'bot':
            bot = int(inst[6])
            bots[bot] = bots.get(bot, [])
            bots[bot].append(lo)
        elif inst[5] == 'output':
            output_id = int(inst[6])
            outputs[output_id] = lo
        if inst[10] == 'bot':
            bot = int(inst[11])
            bots[bot] = bots.get(bot, [])
            bots[bot].append(hi)
        elif inst[10] == 'output':
            output_id = int(inst[11])
            outputs[output_id] = hi
    else:
        print('Cannot understand', inst)
        break

print(outputs[0]*outputs[1]*outputs[2])
