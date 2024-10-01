#!/usr/bin/python3
'''
This module provides a function that decodes JSON to an object.
'''
import json


def from_json_string(my_str):
    '''
    Returns an object representation from a JSON string.
    Args:
        my_str (string): The JSON string to process.

    Returns:
        An object containing the same data as the JSON.
    '''
    return json.loads(my_str)
