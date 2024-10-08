#!/usr/bin/python3
"""
This module contains the text_indentation function.
"""

def text_indentation(text):
    """
    Prints a text with two new lines after each of the following characters: '.', '?', ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    while i < len(text) and text[i] == ' ':
        i += 1

    while i < len(text):
        print(text[i], end="")
        if text[i] == "\n" or text[i] in ".?:":
            if text[i] in ".?:":
                print("\n")
            i += 1
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
