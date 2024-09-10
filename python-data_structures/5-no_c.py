#!/usr/bin/python3

def no_c(my_string):
    result = ''
    chars_to_remove = "cC"
    for char in my_string:
        if char not in chars_to_remove:
            result += char
    return (result)
