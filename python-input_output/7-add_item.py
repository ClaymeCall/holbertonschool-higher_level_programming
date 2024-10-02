#!/usr/bin/python3
'''
This module provides a function that writes all its arguments
to a JSON file
'''
import json
import sys
from os import path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = 'add_item.json'

if path.exists(filename):
    object = load_from_json_file(filename)
else:
    object = []

object.extend(sys.argv[1:])

save_to_json_file(object, filename)
