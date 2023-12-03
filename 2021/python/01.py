with open('../input/01.txt') as stream:
    d = [int(line) for line in stream.readlines()]

increasing = 0
for i in range(len(d)):
    if i > 0 and d[i] > d[i-1]:
        increasing += 1
print(increasing)

increasing = 0
for i in range(len(d)):
    if i > 3 and (d[i] + d[i-1] + d[i-2]) > (d[i-1] + d[i-2] + d[i-3]):
        increasing += 1
print(increasing)
