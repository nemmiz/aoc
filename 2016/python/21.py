#!/usr/bin/python3


def scramble(password, instructions):
    password = list(password)
    for inst in instructions:
        if inst[0] == 'swap':
            if inst[1] == 'position':
                a = int(inst[2])
                b = int(inst[5])
            elif inst[1] == 'letter':
                a = password.index(inst[2])
                b = password.index(inst[5])
            tmp = password[a]
            password[a] = password[b]
            password[b] = tmp
        elif inst[0] == 'rotate':
            if inst[1] == 'left':
                a = int(inst[2])
            elif inst[1] == 'right':
                a = -int(inst[2])
            elif inst[1] == 'based':
                a = password.index(inst[6])
                password = password[-1:] + password[:-1]
                if a >= 4:
                    a += 1
                a = -a
            password = password[a:] + password[:a]
        elif inst[0] == 'reverse':
            a = int(inst[2])
            b = int(inst[4])
            password = password[:a] + list(reversed(password[a:b+1])) + password[b+1:]
        elif inst[0] == 'move':
            a = int(inst[2])
            b = int(inst[5])
            tmp = password.pop(a)
            password.insert(b, tmp)
        else:
            print('Unknown instruction:', inst)
    print(''.join(password))


def unscramble(password, instructions):
    password = list(password)
    for inst in reversed(instructions):
        if inst[0] == 'swap':
            if inst[1] == 'position':
                a = int(inst[2])
                b = int(inst[5])
            elif inst[1] == 'letter':
                a = password.index(inst[2])
                b = password.index(inst[5])
            tmp = password[a]
            password[a] = password[b]
            password[b] = tmp
        elif inst[0] == 'rotate':
            if inst[1] == 'left':
                a = -int(inst[2])
                password = password[a:] + password[:a]
            elif inst[1] == 'right':
                a = int(inst[2])
                password = password[a:] + password[:a]
            elif inst[1] == 'based':
                pos_after = password.index(inst[6])
                while True:
                    password = password[1:] + password[:1]
                    a = password.index(inst[6])
                    b = a
                    if a >= 4:
                        a += 1
                    a += b
                    a = (a + 1) % len(password)
                    if a == pos_after:
                        break
        elif inst[0] == 'reverse':
            a = int(inst[2])
            b = int(inst[4])
            password = password[:a] + list(reversed(password[a:b+1])) + password[b+1:]
        elif inst[0] == 'move':
            a = int(inst[5])
            b = int(inst[2])
            tmp = password.pop(a)
            password.insert(b, tmp)
        else:
            print('Unknown instruction:', inst)
    print(''.join(password))


with open('../input/21.txt') as f:
    instructions = [tuple(line.split()) for line in f.readlines()]

scramble('abcdefgh', instructions)
unscramble('fbgdceah', instructions)
