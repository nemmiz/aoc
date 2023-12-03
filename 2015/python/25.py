#!/usr/bin/python3

x, y = 1, 1
code = 20151125

while not (x == 3029 and y == 2947):
    if y == 1:
        y = x + 1
        x = 1
    else:
        y -= 1
        x += 1
    code *= 252533
    code %= 33554393

print(code)
