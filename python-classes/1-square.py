#!/usr/bin/python3
"""
1-square.py

This module provides a Square class.
"""


class Square:
    """
    Defines a Square object.

    Attributes:
        size (no type): The size of the square.
    """

    def __init__(self, size):
        """
        Initialize the square with a certain size.

        Args:
            size (no type): The size of the square.
        """
        self.__size = size
