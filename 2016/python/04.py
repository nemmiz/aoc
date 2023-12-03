#!/usr/bin/python3

def real_room(encrypted):
    last_dash = encrypted.rfind('-')
    letters = encrypted[:last_dash].replace('-', '')
    sector_id = int(encrypted[last_dash+1:-7])
    checksum = encrypted[-6:-1]

    counts = [100] * 26
    for c in letters:
        counts[ord(c) - ord('a')] -= 1
    tmp = sorted(list(zip(counts, 'abcdefghijklmnopqrstuvwxyz')))
    calculated_checksum = ''.join((x[1] for x in tmp[:5]))

    return sector_id if calculated_checksum == checksum else 0


def decode_name(encrypted):
    last_dash = encrypted.rfind('-')
    words = encrypted[:last_dash].split('-')
    sector_id = int(encrypted[last_dash+1:-7])

    decoded = []
    for word in words:
        for c in word:
            n = ord(c) - ord('a')
            n += sector_id
            n %= 26
            n += ord('a')
            decoded.append(chr(n))
        decoded.append(' ')
    return ''.join(decoded[:-1]), sector_id


with open('../input/04.txt') as f:
    rooms = [line.strip() for line in f.readlines()]

print(sum(map(real_room, rooms)))

for room in rooms:
    name, sector_id = decode_name(room)
    if 'northpole' in name:
        print(sector_id)
