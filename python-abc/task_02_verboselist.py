#!/usr/bin/python3

from abc import ABC, abstractmethod


class VerboseList(list):
    def append(self, item=None):
        super().append(item)
        print("Added [{}] to the list.".format(item))

    def extend(self, items=[]):
        super().extend(items)
        
        print("Extended the list with [{}] items.".format(len(items)))

    def remove(self, item=None):
        super().remove(item)
        print("Removed [{}] from the list.".format(item))

    def pop(self, index=-1):
        item = super().pop(index)
        print("Popped [{}] from the list.".format(item))
