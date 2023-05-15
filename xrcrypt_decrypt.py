#!/usr/bin/env python3

import sys

if len(sys.argv) != 2:
    print("Usage: {} [encrypted file].".format(sys.argv[0]))
    sys.exit(1)

try:
    with open(sys.argv[1], 'r') as in_file:
        in_stream = [int(n) for n in in_file.read().split('.') if n]
except IOError:
    sys.stderr.write("Could not open file {}\n".format(sys.argv[1]))
    sys.exit(1)

i = 0
encrypted_char = 0
raw_outstream = []
for n in in_stream:  # Find the encoded number for each character of the message
    encrypted_char += n
    i += 1
    if not i % 3:
        raw_outstream.append(encrypted_char)
        encrypted_char = 0

# First subtraction factor - min value for an ASCII char not lower than 0
key = min(raw_outstream)
in_char = ''
while not in_char == 'q':
    out_stream = ''.join([chr(c - key) for c in raw_outstream])  # Decoding attempts
    print(out_stream)
    in_char = input('Enter any character (or \'q\' to exit) > ')
    key -= 1

sys.exit(0)
