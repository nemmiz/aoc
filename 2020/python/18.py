import re

class NumA:
    """ Number where the - operator acts as * """
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return NumA(self.x + other.x)
    def __sub__(self, other):
        return NumA(self.x * other.x)
    def to_int(self):
        return self.x

class NumB:
    """ Number where the + and * operators are flipped """
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return NumB(self.x * other.x)
    def __mul__(self, other):
        return NumB(self.x + other.x)
    def to_int(self):
        return self.x

def evaluate1(lines):
    acc = 0
    for line in lines:
        line = line.replace('*', '-')
        tmp = re.sub(r'(\d+)', r'NumA(\1)', line)
        acc += eval(tmp).to_int()
    return acc

def evaluate2(lines):
    acc = 0
    for line in lines:
        line = line.replace('+', '%')
        line = line.replace('*', '+')
        line = line.replace('%', '*')
        tmp = re.sub(r'(\d+)', r'NumB(\1)', line)
        acc += eval(tmp).to_int()
    return acc

with open('../input/18.txt') as stream:
    lines = [line.strip() for line in stream]

print(evaluate1(lines))
print(evaluate2(lines))
