#!/usr/bin/env python

# This script will violate every message enciphered with an affine cipher
# it does a simple 'brute force' attack

import sys
import os

# This function calculates the modular inverse of a number
def mod_inv (num, mod):
    for x in range(0,mod + 1):
        if ((num*x)%mod == 1):
            return x
    sys.exit('[!!!] ERROR: modulo %d inverse of %d does not exists!' % (mod, num))

# Checking arguments
if not len(sys.argv) == 2:
    sys.exit('Usage: %s [crypted message]\nExecutes a brute force attack on the ciphered message.' % sys.argv[0])

if sys.argv[1] == '-h' or sys.argv[1] == '--help':
    sys.exit('Usage: %s [crypted message]\nExecutes a brute force attack on the ciphered message.' % sys.argv[0])

# Setting input code
code = sys.argv[1]

# Brute force algorithm
for i in range(0, 26):
    if (i % 2 != 0) and (i != 13):
        for j in range(0, 26):
            print('\n# TRYING KEY <%d,%d>\n# MESSAGE :' % (i, j))
            inv = mod_inv(i, 26)
            for c in code:
                v = ord(c)
                if (v >= 65) and (v <= 90):
                    # uppercase
                    cip = ((v - 65 - j) * inv + 26) % 26 + 65
                elif (v >= 97) and (v <= 122):
                    # lowercase
                    cip = ((v - 97 - j) * inv + 26) % 26 + 97
                else:
                    # other characters
                    cip = v
                # writing deciphered character
                print(chr(cip), end='')
            print()