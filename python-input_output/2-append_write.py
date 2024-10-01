#!/usr/bin/python3
'''
This modules provides a function that appends to a file.
'''


def append_write(filename="", text=""):
    '''
    Appends text to a text file (UTF8).

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The text to append. Defaults to "".

    Returns:
        The number of characters appended
    '''
    with open(filename, 'a', encoding='utf-8') as file:
        return (file.write(text))
