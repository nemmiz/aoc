import io

def decode_packets(bitstream):
    pver = int(bitstream.read(3), 2)
    ptyp = int(bitstream.read(3), 2)

    if ptyp == 4:
        binnum = ''
        while True:
            group = bitstream.read(5)
            binnum += group[1:]
            if group[0] == '0':
                break
        return (pver, ptyp, int(binnum, 2))
    
    elif bitstream.read(1) == '0':
        length_of_subpackets = int(bitstream.read(15), 2)
        current_pos = bitstream.tell()
        subpackets = []
        while bitstream.tell() < (current_pos + length_of_subpackets):
            subpackets.append(decode_packets(bitstream))
        return (pver, ptyp, subpackets)

    else:
        number_of_subpackets = int(bitstream.read(11), 2)
        subpackets = []
        for _ in range(number_of_subpackets):
            subpackets.append(decode_packets(bitstream))
        return (pver, ptyp, subpackets)

def decode(transmission):
    bits = ''.join([f'{int(hexdigit, 16):b}'.zfill(4) for hexdigit in transmission])
    return decode_packets(io.StringIO(bits))

def version_sum(packet):
    result = packet[0]
    if packet[1] != 4:
        for subpacket in packet[2]:
            result += version_sum(subpacket)
    return result

def eval_packet(packet):
    if packet[1] == 0:
        return sum(eval_packet(subpacket) for subpacket in packet[2])
    elif packet[1] == 1:
        product = 1
        for subpacket in packet[2]:
            product *= eval_packet(subpacket)
        return product
    elif packet[1] == 2:
        return min(eval_packet(subpacket) for subpacket in packet[2])
    elif packet[1] == 3:
        return max(eval_packet(subpacket) for subpacket in packet[2])
    elif packet[1] == 4:
        return packet[2]
    else:
        a = eval_packet(packet[2][0])
        b = eval_packet(packet[2][1])
        if packet[1] == 5:
            return 1 if a > b else 0
        if packet[1] == 6:
            return 1 if a < b else 0
        if packet[1] == 7:
            return 1 if a == b else 0

with open('../input/16.txt') as stream:
    transmission = stream.read().strip()

print(version_sum(decode(transmission)))
print(eval_packet(decode(transmission)))
