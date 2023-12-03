#!/usr/bin/python3

def uncompressed_len(data, times, recurse):
    total = 0
    while data:
        paran_start = data.find('(')
        if paran_start == -1:
            total += len(data)
            break
        paran_end = data.find(')')
        nchars, times2 = map(int, data[paran_start+1:paran_end].split('x'))
        chars = data[paran_end+1:paran_end+1+nchars]
        data = data[paran_end+1+nchars:]
        if recurse:
            total += uncompressed_len(chars, times2, recurse)
        else:
            total += len(chars) * times2
    return total * times

with open('../input/09.txt') as f:
    input_data = f.read()

print(uncompressed_len(input_data, 1, recurse=False))
print(uncompressed_len(input_data, 1, recurse=True))
