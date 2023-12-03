#!/usr/bin/python3

def split_ip(ip):
    outside = []
    inside = []
    while True:
        start_index = ip.find('[')
        if start_index == -1:
            outside.append(ip)
            break
        end_index = ip.find(']')
        outside.append(ip[:start_index])
        inside.append(ip[start_index+1:end_index])
        ip = ip[end_index+1:]
    return inside, outside


def has_abba(s):
    for i in range(3, len(s)):
        if s[i-3] == s[i] and s[i-2] == s[i-1] and s[i] != s[i-1]:
            return True
    return False

def supports_tls(ip):
    inside, outside = split_ip(ip)

    for seq in inside:
        if has_abba(seq):
            return False

    for seq in outside:
        if has_abba(seq):
            return True

    return False


def find_abas(seqs):
    abas = set()
    for seq in seqs:
        for i in range(2, len(seq)):
            if seq[i-2] == seq[i] and seq[i] != seq[i-1]:
                abas.add(seq[i-2:i+1])
    return abas

def abas_to_babs(abas):
    babs = set()
    for aba in abas:
        babs.add(aba[1]+aba[0]+aba[1])
    return babs

def supports_ssl(ip):
    inside, outside = split_ip(ip)

    babs = abas_to_babs(find_abas(outside))

    for seq in inside:
        for bab in babs:
            if bab in seq:
                return True

    return False


with open('../input/07.txt') as f:
    messages = [line.strip() for line in f.readlines()]

tls, ssl = 0, 0
for message in messages:
    if supports_tls(message):
        tls += 1
    if supports_ssl(message):
        ssl += 1

print(tls)
print(ssl)
