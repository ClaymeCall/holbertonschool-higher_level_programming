#!/usr/bin/python3

'''
This module contains a class that inherits from List.
'''


class MyList:
    '''
    This class prints itself in ascending order.
    '''

    def print_sorted(self):
        '''
        This method prints the contents of the current instance calling it.
        '''
        print(sorted(self))
