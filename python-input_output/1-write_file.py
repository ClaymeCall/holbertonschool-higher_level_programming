#!/usr/bin/python3
'''
This modules provides a function that writes in a file.
'''


def write_file(filename="", text=""):
    '''
    Writes text in a text file (UTF8).

    Args:
        filename (str): The name of the file to write. Defaults to "".
        text (str): The text to write. Defaults to "".

    Returns:
        The number of characters written
    '''
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
