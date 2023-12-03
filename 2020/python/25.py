def transform(subject_number, loop_size):
    value = 1
    for i in range(loop_size):
        value *= subject_number
        value %= 20201227
    return value

def find_loop_size(target):
    value = 1
    loop_size = 0
    while True:
        value *= 7
        value %= 20201227
        loop_size += 1
        if value == target:
            return loop_size

key1 = 19774466
key2 = 7290641

loop_size1 = find_loop_size(key1)
loop_size2 = find_loop_size(key2)

if loop_size1 < loop_size2:
    print(transform(key2, loop_size1))
else:
    print(transform(key1, loop_size2))
    