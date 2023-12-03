#!/usr/bin/python3

def paper_needed(dimensions):
    l, w, h = (int(x) for x in dimensions.split('x'))
    sides = (l*w, w*h, h*l)
    return sides[0]*2 + sides[1]*2 + sides[2]*2 + min(sides)

def ribbon_needed(dimensions):
    l, w, h = (int(x) for x in dimensions.split('x'))
    return min(l+l+w+w, w+w+h+h, h+h+l+l) + l*w*h

with open('../input/02.txt') as f:
    presents = [line.strip() for line in f]

print(sum(map(paper_needed, presents)))
print(sum(map(ribbon_needed, presents)))
