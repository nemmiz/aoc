#!/usr/bin/python3

def part1(molecule, replacements):
    new_molecules = set()
    for r in replacements:
        i = 0
        while True:
            i = molecule.find(r[0], i)
            if i == -1:
                break
            new_molecule = molecule[:i] + r[1] + molecule[i+len(r[0]):]
            new_molecules.add(new_molecule)
            i += 1
    print(len(new_molecules))

def part2(molecule, replacements):
    simplifications = []
    end_states = set()
    for src, dst in replacements:
        if src == 'e':
            end_states.add(dst)
        else:
            simplifications.append((dst, src))

    total = 0
    while molecule not in end_states:
        for src, dst in simplifications:
            i = molecule.find(src)
            if i != -1:
                molecule = molecule.replace(src, dst, 1)
                total += 1
                break
    print(total+1)

with open('../input/19.txt') as f:
    lines = [line.strip() for line in f.readlines()]
    molecule = lines[-1]
    replacements = []
    for line in lines[:-2]:
        parts = line.split()
        replacements.append((parts[0], parts[2]))

part1(molecule, replacements)
part2(molecule, replacements)
