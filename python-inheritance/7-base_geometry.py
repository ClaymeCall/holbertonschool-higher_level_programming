#!/usr/bin/python3
'''
This modules provides a BaseGeometry class.
'''


class BaseGeometry():
    '''
    Empty base geometry class.
    '''
    def area(self):
        '''
        Empty method that raises an exception as its not yet implemented.
        '''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
