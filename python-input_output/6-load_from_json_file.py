#!/usr/bin/python3
'''
This module provides a function that retrieves JSON from a file
and returns an object from it.
'''
import json


def load_from_json_file(filename):
    '''
    Returns an object from a JSON file.

    Args:
        filename (string): the file to read

    Returns:
        None
    '''
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)
