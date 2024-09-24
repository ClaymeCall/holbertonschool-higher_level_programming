#!/usr/bin/python3
'''
Defines a class checking function.
'''


def is_same_class(obj, a_class):
    '''
    Tests wether an object is matching a certain class

    Args:
    obj: the object to test.
    a_class: the class to test the objects type against.

    Returns: True if types match, False otherwise
    '''
    res = type(obj) is a_class
    return res
