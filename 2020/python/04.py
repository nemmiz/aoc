import re

def read_passports(lines):
    passports = []
    current = {}
    for line in lines:
        if line:
            for pair in line.split():
                k, v = pair.split(':')
                current[k] = v
        else:
            passports.append(current)
            current = {}
    if current:
        passports.append(current)
    return passports

def validate_passport_1(passport):
    for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
        if field not in passport:
            return False
    return True

def validate_passport_2(passport):
    field = int(passport.get('byr', '0'))
    if field < 1920 or field > 2002:
        return False
    field = int(passport.get('iyr', '0'))
    if field < 2010 or field > 2020:
        return False
    field = int(passport.get('eyr', '0'))
    if field < 2020 or field > 2030:
        return False
    field = passport.get('hgt', '')
    if field.endswith('cm'):
        hgt = int(field[:-2])
        if hgt < 150 or hgt > 193:
            return False
    elif field.endswith('in'):
        hgt = int(field[:-2])
        if hgt < 59 or hgt > 76:
            return False
    else:
        return False
    field = passport.get('hcl', '')
    if not re.fullmatch(r'#[0-9a-f]{6}', field):
        return False
    field = passport.get('ecl', '')
    if field not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    field = passport.get('pid', '')
    if not re.fullmatch(r'[0-9]{9}', field):
        return False
    return True


with open('../input/04.txt') as stream:
    lines = [line.strip() for line in stream]

passports = read_passports(lines)
num_ok_1 = 0
num_ok_2 = 0

for passport in passports:
    if validate_passport_1(passport):
        num_ok_1 += 1
    if validate_passport_2(passport):
        num_ok_2 += 1

print(num_ok_1)
print(num_ok_2)
