#!/usr/bin/python3

def inc(numbers):
    i = len(numbers) - 1
    while i >= 0:
        numbers[i] += 1
        if numbers[i] in (105, 111, 108):
            numbers[i] += 1
            break
        elif numbers[i] > 122:
            numbers[i] -= 26
            i -= 1
        else:
            break

def valid(numbers):
    for i in range(2, len(numbers)):
        if numbers[i-2] == (numbers[i]-2) and numbers[i-1] == (numbers[i]-1):
            break
    else:
        return False

    pairs, i = 0, 1
    while i < len(numbers):
        if numbers[i-1] == numbers[i]:
            pairs += 1
            i += 2
        else:
            i += 1
    return pairs >= 2
        
def next_password(password):
    numbers = [ord(c) for c in password]
    while True:
        inc(numbers)
        if valid(numbers):
            return ''.join([chr(x) for x in numbers])

password = next_password('cqjxjnds')
print(password)

password = next_password(password)
print(password)
