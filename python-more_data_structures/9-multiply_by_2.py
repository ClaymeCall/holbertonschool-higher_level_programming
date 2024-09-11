#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    mul_dict = dict(a_dictionary)

    for key in mul_dict:
        mul_dict[key] *= 2

    return mul_dict
