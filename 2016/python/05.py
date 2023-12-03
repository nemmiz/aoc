#!/usr/bin/python3

import hashlib
import itertools

secret = 'ugkcyxxp'

password1 = []
password2 = ['_'] * 8

for i in itertools.count():
    result = hashlib.md5((secret + str(i)).encode('ascii')).hexdigest()
    if result.startswith('00000'):
        # Crack password 1
        if len(password1) < 8:
            password1.append(result[5])
            
        # Crack password 2
        pos = result[5]
        val = result[6]
        if pos.isdecimal():
            pos = int(pos)
            if pos < 8 and password2[pos] == '_':
                password2[pos] = val

        # Check if both passwords are done
        if len(password1) == 8 and '_' not in password2:
            break

print(''.join(password1))
print(''.join(password2))
