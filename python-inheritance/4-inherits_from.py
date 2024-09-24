#!/usr/bin/python3
'''
Defines a class checking function.
'''


def inherits_from(obj, a_class):
    '''
    Tests wether an object is matching a inherited class

    Args:
    obj: the object to test.
    a_class: the class to test the objects type against.

    Returns: True if types match, False otherwise
    '''
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False
