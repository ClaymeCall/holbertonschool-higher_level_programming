#!/usr/bin/python3

def uppercase(str):
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            print("{}".format(chr(ord(c) - 32)))
        else:
            print("{}".format(c))
