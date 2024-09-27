#!/usr/bin/python3
'''
This module provides an abstract class Shape
and two subclasses that can return their respective area and perimeter.
'''

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        ...
    @abstractmethod
    def perimeter(self):
        ...


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (2 * self.width) + (2 * self.height)


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()

    print("Area: {}".format(area))
    print("Perimeter: {}".format(perimeter))
