#!/usr/bin/python3

def is_same_class(obj, a_class):
    '''
    Tests wether an object is matching a certain class.

    Arguments:
    obj: the object to test.
    a_class: the class to test the objects type against.
    '''
    res = type(obj) is a_class
    return res
