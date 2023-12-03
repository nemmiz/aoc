def bbox(image):
    minx, miny = 99999999999999, 99999999999999
    maxx, maxy = -9999999999999, -9999999999999
    for x, y in image:
        minx = min(minx, x)
        miny = min(miny, y)
        maxx = max(maxx, x)
        maxy = max(maxy, y)
    return minx, miny, maxx, maxy

def enhance(image, algorithm, flash):
    minx, miny, maxx, maxy = bbox(image)
    output = set()
    for y in range(miny-1, maxy+2):
        for x in range(minx-1, maxx+2):
            num = 0
            for yy in range(y-1, y+2):
                for xx in range(x-1, x+2):
                    num <<= 1
                    if flash and (xx < minx or yy < miny or xx > maxx or yy > maxy):
                        num |= 1
                    elif (xx, yy) in image:
                        num |= 1
            if algorithm[num] == '#':
                output.add((x, y))
    return output

with open('../input/20.txt') as stream:
    lines = [line.strip() for line in stream.readlines()]
    algorithm = lines[0]

    image = set()
    for y, line in enumerate(lines[2:]):
        for x, pixel in enumerate(line):
            if pixel == '#':
                image.add((x, y))

for i in range(50):
    if i == 2:
        print(len(image))
    image = enhance(image, algorithm, algorithm[0] == '#' and i % 2 == 1)
print(len(image))
