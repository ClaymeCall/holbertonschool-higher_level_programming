#!/usr/bin/python3
'''
This module provides an abstract class animal
and two subclasses that can return their respective sound.
'''

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        ...

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
