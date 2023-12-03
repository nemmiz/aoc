#!/usr/bin/python3

from collections import deque

def part1(n):
    queue = deque(i+1 for i in range(n))

    while queue:
        elf = queue.popleft()

        if queue:
            elf2 = queue.popleft()
            queue.append(elf)
        else:
            print('Elf', elf, 'wins')
            break

def part2(n):
    queue1 = deque(i+1 for i in range(0, n//2))
    queue2 = deque(i+1 for i in range(n//2, n))

    while queue1:
        elf = queue1.popleft()

        if queue2:
            if len(queue1) >= len(queue2):
                elf2 = queue1.pop()
            else:
                elf2 = queue2.popleft()

            queue2.append(elf)
            queue1.append(queue2.popleft())
        else:
            print('Elf', elf, 'wins')
            break

part1(3017957)
part2(3017957)
