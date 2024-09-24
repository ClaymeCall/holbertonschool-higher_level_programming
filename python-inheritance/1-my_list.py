#!/usr/bin/python3

'''
This module contains a class that inherits from List.
'''


class MyList(list):
    '''
    This class prints itself in ascending order.
    '''
    def __init__(self):
        '''
        Initializes a new instance
        '''
        super().__init__()

    def print_sorted(self):
        '''
        This method prints the contents of the current instance calling it.
        '''
        print(sorted(self))
