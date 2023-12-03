#!/usr/bin/python3

def part1(passphrases):
    total = 0
    for passphrase in passphrases:
        unique = set(passphrase)
        if len(passphrase) == len(unique):
            total += 1
    print(total)

def part2(passphrases):
    total = 0
    for passphrase in passphrases:
        words = [frozenset(word) for word in passphrase]
        unique = set(words)
        if len(words) == len(unique):
            total += 1
    print(total)

with open('../input/04.txt') as f:
    passphrases = [line.split() for line in f.readlines()]

part1(passphrases)
part2(passphrases)
