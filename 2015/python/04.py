#!/usr/bin/python3

import hashlib
import itertools

secret = 'ckczppom'

for i in itertools.count():
    result = hashlib.md5((secret + str(i)).encode('ascii')).hexdigest()
    if result.startswith('00000'):
        print(i)
        break

for i in itertools.count():
    result = hashlib.md5((secret + str(i)).encode('ascii')).hexdigest()
    if result.startswith('000000'):
        print(i)
        break
