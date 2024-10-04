#!/usr/bin/python3
'''
This module provides a function that pickles instances of data to a file.
'''
import pickle


class CustomObject():
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        '''
        Pickles the object in a file.

        Args:
            data (dict): The data to process.
            filename (string): the file to write

        Returns:
            None
        '''
        try:
            with open(filename, 'wb', ) as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        '''
        Returns an object from a pkl file.

        Args:
            filename (string): the name of the binary file to read

        Returns:
            deserialized object
        '''
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
