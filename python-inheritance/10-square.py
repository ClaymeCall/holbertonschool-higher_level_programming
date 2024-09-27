#!/usr/bin/python3
'''
This module provides a Square classe.
'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''
    Represents a Square.

    Attributes:
        size (int): The size of the Square.
    '''

    def __init__(self, size):
        """
        Initialize the Square with a certain size.

        Args:
            size (int): The size of the Square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return a string representation of the square."""
        return "[{}] {}/{}".format(type(self)._name_, self._size, self._size)
