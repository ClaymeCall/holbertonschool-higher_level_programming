#!/usr/bin/python3

alphabet_indexes = range(ord('a'), ord('z') + 1)
for i in alphabet_indexes:
    if chr(i) != 'e' and chr(i) != 'q':
        print("{}".format(chr(i)), end="")
