#!/usr/bin/python3
"""
6-square.py

This module provides a Square class.
It includes methods to return size, area, set a new size, and print the square.
"""


class Square:
    """
    Defines a Square object.

    Attributes:
        size (int): The size of the square.
        position (int): The size of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a certain size.

        Args:
            size (int): The size of the square.
            position (int): The position of the square
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """ Returns the position of the square """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of square

        Attribut:
        value (int): Tuple storing the coordinates
        """
        err_msg = "position must be a tuple of 2 positive integers"

        if type(value) is not tuple or len(value) != 2:
            raise TypeError(err_msg)

        for num in value:
            if type(num) is not int or num < 0:
                raise TypeError(err_msg)

        self.__position = value

    def area(self):
        """
        Returns the area of the current square.

        Args:
        self (Square): Current instance of Square object.

        Return:
        Area of the square, as int.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the current square.

        Args:
        self (Square): Current instance of Square object.
        """
        if self.__size == 0:
            print()

        else:
            print("\n" * self.__position[1], end="")

            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
