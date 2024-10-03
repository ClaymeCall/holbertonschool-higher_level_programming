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

    def to_json(self, attrs=None):
        '''
        Returns a dictionary description of the student instance

        Args:
            self: the current instance of Student

        Returns:
            Dictionary description of the instance
        '''

        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
        else:
            return self.__dict__

    def reload_from_json(self, json):
        '''
        Loads attributes from a dictionary

        Args:
            self: the current instance of Student
            json: the dictionnary to load

        Returns:
            None
        '''
        for key, value in json.items():
            setattr(self, key, value)
