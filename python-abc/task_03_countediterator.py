#!/usr/bin/python3


class CountedIterator:
    
    def __init__(self, obj):
        self.obj = iter(obj)
        self.counter = 0

    def __next__(self):
        try:
            next_item = next(self.obj)
            self.counter += 1
            return next_item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.counter
