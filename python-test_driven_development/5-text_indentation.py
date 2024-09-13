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

    result = ""
    i = 0
    while i < len(text):
        result += text[i]
        if text[i] in {'.', '?', ':'}:
            result += "\n\n"
            while i + 1 < len(text) and text[i + 1] == ' ':
                i += 1
        i += 1
    
    print(result.strip())
