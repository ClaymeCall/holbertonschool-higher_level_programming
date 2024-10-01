#!/usr/bin/python3
'''
This modules provides a function that appends to a file.
'''
import json


def to_json_string(my_obj):
    '''
    Returns a JSON representation of an object.

    Args:
        my_obj (object): The object to process.

    Returns:
        JSON representation of the object.
    '''
    return json.dumps(my_obj)
