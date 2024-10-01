#!/usr/bin/python3
'''
This module provides a function that writes JSON to a file.
'''
import json


def save_to_json_file(my_obj, filename):
    '''
    Writes a JSON representation of an object in a file.

    Args:
        my_obj (object): The object to process.
        filename (string): the file to write

    Returns:
        None
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
