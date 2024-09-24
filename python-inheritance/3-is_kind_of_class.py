#!/usr/bin/python3
'''
Defines a class checking function.
'''


def is_kind_of_class(obj, a_class):
    '''
    Tests wether an object is matching a certain class or inherited one

    Args:
    obj: the object to test.
    a_class: the class to test the objects type against.

    Returns: True if types match, False otherwise
    '''
    return isinstance(obj, a_class)
