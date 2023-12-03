import sys

def turn(facing, direction, degrees):
    if degrees not in [90, 180, 270]:
        sys.exit('invalid angle: ' + degrees)
    CLOCKWISE = ['N', 'E', 'S', 'W']
    cwindex = CLOCKWISE.index(facing)
    if direction == 'R':
        cwindex += (degrees // 90)
        if cwindex > 3:
            cwindex -= 4
    elif direction == 'L':
        cwindex -= (degrees // 90)
        if cwindex < 0:
            cwindex += 4
    return CLOCKWISE[cwindex]

def rotate_waypoint(wp_off, direction, degrees):
    if degrees not in [90, 180, 270]:
        sys.exit('invalid angle: ' + degrees)
    if direction == 'L':
        if degrees == 90:
            degrees = 270
        elif degrees == 270:
            degrees = 90
    if degrees == 90:
        wp_off = (-wp_off[1], wp_off[0])
    elif degrees == 180:
        wp_off = (-wp_off[0], -wp_off[1])
    elif degrees == 270:
        wp_off = (wp_off[1], -wp_off[0])
    return wp_off

def part1(directions):
    facing = 'E'
    pos = (0, 0)
    for direction, steps in directions:
        if direction == 'N':
            pos = (pos[0], pos[1]-steps)
        elif direction == 'S':
            pos = (pos[0], pos[1]+steps)
        elif direction == 'E':
            pos = (pos[0]+steps, pos[1])
        elif direction == 'W':
            pos = (pos[0]-steps, pos[1])
        elif direction in 'LR':
            facing = turn(facing, direction, steps)
        elif direction == 'F':
            if facing == 'N':
                pos = (pos[0], pos[1]-steps)
            elif facing == 'S':
                pos = (pos[0], pos[1]+steps)
            elif facing == 'E':
                pos = (pos[0]+steps, pos[1])
            elif facing == 'W':
                pos = (pos[0]-steps, pos[1])
    print(abs(pos[0]) + abs(pos[1]))

def part2(directions):
    pos = (0, 0)
    wp_off = (10, -1)
    for direction, steps in directions:
        if direction == 'N':
            wp_off = (wp_off[0], wp_off[1]-steps)
        elif direction == 'S':
            wp_off = (wp_off[0], wp_off[1]+steps)
        elif direction == 'E':
            wp_off = (wp_off[0]+steps, wp_off[1])
        elif direction == 'W':
            wp_off = (wp_off[0]-steps, wp_off[1])
        elif direction in 'LR':
            wp_off = rotate_waypoint(wp_off, direction, steps)
        elif direction == 'F':
            pos = (pos[0]+wp_off[0]*steps, pos[1]+wp_off[1]*steps)
    print(abs(pos[0]) + abs(pos[1]))

with open('../input/12.txt') as stream:
    directions = [(line[0], int(line[1:])) for line in stream]

part1(directions)
part2(directions)
