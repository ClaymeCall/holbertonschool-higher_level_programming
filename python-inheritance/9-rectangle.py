#!/usr/bin/python3
'''
This module provides a Rectangle class that inherits from BaseGeometry class.
'''


class BaseGeometry:
    """Represent base geometry."""

    def area(self):
        """Exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        Returns:
            value if no raises.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

        return value


class Rectangle(BaseGeometry):
    '''
    Represents a rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
    '''

    def __init__(self, width, height):
        """
        Initialize the rectangle with a certain size.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
        """
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        classname = self.__class__.__name__
        str = "[{}] {}/{}".format(classname, self.__width, self.__height)
        return str
