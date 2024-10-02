#!/usr/bin/python3
'''
This module provides a function that prepares an object
for JSON serialization.
'''


def class_to_json(obj):
    '''
    Returns an dictionary description of an object

    Args:
        obj: the object to serialize

    Returns:
        Dictionary description of obj
    '''
    return obj.__dict__
