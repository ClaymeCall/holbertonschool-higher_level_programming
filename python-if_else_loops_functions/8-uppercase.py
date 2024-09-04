#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            char_to_print = chr(ord(c) - 32)
        else:
            char_to_print = c
        print("{}".format(char_to_print), end='')
    print("")
