#!/usr/bin/python3

with open('../input/08.txt') as f:
    instructions = [line.strip() for line in f.readlines()]

screen_w = 50
screen_h = 6
screen = ['.'] * (screen_w * screen_h)

for inst in instructions:
    if inst.startswith('rect '):
        inst = inst[5:]
        w, h = map(int, inst.split('x'))
        for y in range(h):
            for x in range(w):
                screen[y*screen_w+x] = '#'

    elif inst.startswith('rotate column x='):
        inst = inst[16:]
        x, amt = map(int, inst.split(' by '))
        column = [screen[y*screen_w+x] for y in range(screen_h)]
        for i, pixel in enumerate(column):
            y = (amt + i) % screen_h
            screen[y*screen_w+x] = pixel

    elif inst.startswith('rotate row y='):
        inst = inst[13:]
        y, amt = map(int, inst.split(' by '))
        row = [screen[y*screen_w+x] for x in range(screen_w)]
        for i, pixel in enumerate(row):
            x = (amt + i) % screen_w
            screen[y*screen_w+x] = pixel

print(screen.count('#'))
for i in range(0, len(screen), screen_w):
    print(''.join(screen[i:i+screen_w]))
