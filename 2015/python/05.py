#!/usr/bin/python3


def is_nice(word):
    # Must contain at least 3 vowels
    if sum((1 for c in word if c in 'aeiou')) < 3:
        return False

    # Must contain at least one letter that appears
    # twice in a row
    for i in range(1, len(word)):
        if word[i] == word[i-1]:
            break
    else:
        return False

    # Must not contain any of these strings
    for s in ['ab', 'cd', 'pq', 'xy']:
        if s in word:
            return False

    return True


def is_nicer(word):
    # Must contain a pair of any two letters that appears
    # at least twice in the string without overlapping
    for i in range(len(word)-2):
        if word.find(word[i:i+2], i+2) != -1:
            break
    else:
        return False
    
    # Must contain at least one letter which repeats
    # with exactly one letter between them
    for i in range(2, len(word)):
        if word[i] == word[i-2]:
            break
    else:
        return False
    
    return True


with open('../input/05.txt') as f:
    words = [line.strip() for line in f.readlines()]

print(sum((1 for word in words if is_nice(word))))
print(sum((1 for word in words if is_nicer(word))))
