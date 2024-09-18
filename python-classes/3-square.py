#!/usr/bin/python3
"""
3-square.py

This module provides a Square class.
"""


class Square:
    """
    Defines a Square object.

    Attributes:
        size (int): The size of the square.
    """

    def __init__(self, size=0):
        """
        Initialize the square with a certain size.

        Args:
            size (no type): The size of the square.
        """
        if type(size) is int:
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size >= 0:
            self.__size = size
        else:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returns the area of the current square.

        Args:
        self (Square): Current instance of Square object.

        Return:
        Area of the square, as int.
        """
        return self.__size ** 2
