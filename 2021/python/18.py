def do_explode(x):
    tmp = x.replace('[', ' [ ').replace(']', ' ] ').replace(',', ' , ').split()
    depth = 0
    
    for i, y in enumerate(tmp):
        if y == '[':
            depth += 1
        elif y == ']':
            depth -= 1
        elif depth > 4 and y.isdigit() and tmp[i+2].isdigit():
            explode_at = i
            num1 = int(tmp[explode_at])
            num2 = int(tmp[explode_at+2])
            break
    else:
        return x

    tmp = tmp[:explode_at-1] + ['0'] + tmp[explode_at+4:]

    for i in range(explode_at-2, -1, -1):
        if tmp[i].isdigit():
            tmp[i] = str(int(tmp[i]) + num1)
            break

    for i in range(explode_at+1, len(tmp)):
        if tmp[i].isdigit():
            tmp[i] = str(int(tmp[i]) + num2)
            break

    return ''.join(tmp)

def do_split(x):
    tmp = x.replace('[', ' [ ').replace(']', ' ] ').replace(',', ' , ').split()
    for i, y in enumerate(tmp):
        if y.isdigit():
            n = int(y)
            if n >= 10:
                num1 = n // 2
                num2 = num1 if n % 2 == 0 else num1+1
                break
    else:
        return x
    
    tmp[i] = f'[{num1},{num2}]'
    return ''.join(tmp)

def do_add(a, b):
    c = f'[{a},{b}]'

    while True:
        tmp = do_explode(c)
        if tmp != c:
            c = tmp
            continue

        tmp = do_split(c)
        if tmp != c:
            c = tmp
            continue

        return c

def magnitude(x):
    return eval(''.join(x.replace('[', '(3*').replace(']', '*2)').replace(',', '+').split()))

def part1(numbers):
    result = numbers[0]
    for line in numbers[1:]:
        result = do_add(result, line)
    print(magnitude(result))

def part2(numbers):
    result = 0
    for x in range(len(lines)):
        for y in range(len(lines)):
            if x != y:
                result = max(result, magnitude(do_add(lines[x], lines[y])))
                result = max(result, magnitude(do_add(lines[y], lines[x])))
    print(result)

with open('../input/18.txt') as stream:
    lines = [line.strip() for line in stream.readlines()]

part1(lines)
part2(lines)
