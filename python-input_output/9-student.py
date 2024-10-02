#!/usr/bin/python3
'''
This module provides a Student class that stores student info.
'''

class Student():
    '''
    Stores student information

    Attributes:
        first_name (string): The first name of the student
        last_name (string): The last name of the student
        age (int): The age of the student
    '''
    def __init__(self, first_name, last_name, age):
        '''
        Initializes an instance of Student

        Args:
        first_name (string): The first name of the student
        last_name (string): The last name of the student
        age (int): The age of the student
        '''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        '''
        Returns an dictionary description of the student instance

        Args:
            self: the current instance of Student

        Returns:
            Dictionary description of the instance
        '''
        return self.__dict__
