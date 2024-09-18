#!/usr/bin/python3
"""
4-square.py

This module provides a Square class.
It includes methods to return size, area, and set a new size.
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

    @property
    def size(self):
        """
        Returns the size of the current squares sides.

        Args:
        self (Square): Current instance of Square object.

        Return:
        Size of the square, as int.
        """
        return self.__size

    def area(self):
        """
        Returns the area of the current square.

        Args:
        self (Square): Current instance of Square object.

        Return:
        Area of the square, as int.
        """
        return self.__size ** 2

    @size.setter
    def size(self, value):
        """
        Sets the size of the current squares sides.

        Args:
        self (Square): Current instance of Square object.
        value (Square): Value to write the new size.
        """
        if type(value) is int:
            self.__size = value
        else:
            raise TypeError("size must be an integer")
        if value >= 0:
            self.__size = value
        else:
            raise ValueError("size must be >= 0")
