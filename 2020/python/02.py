import re
import sys

with open('../input/02.txt') as stream:
    num_ok1 = 0
    num_ok2 = 0
    for line in stream:
        match = re.match(r'(\d+)-(\d+) (\w): (\w+)', line)
        if not match:
            sys.exit(f'No match for line:\n{line}')
        lower = int(match.group(1))
        upper = int(match.group(2))
        char = match.group(3)
        password = match.group(4)

        char_counts = {}
        for ch in password:
            char_counts[ch] = char_counts.get(ch, 0) + 1
        n = char_counts.get(char, 0)
        if n >= lower and n <= upper:
            num_ok1 += 1

        contains = 0
        if password[lower-1] == char:
            contains += 1
        if password[upper-1] == char:
            contains += 1
        if contains == 1:
            num_ok2 += 1
    
    print(num_ok1)
    print(num_ok2)
