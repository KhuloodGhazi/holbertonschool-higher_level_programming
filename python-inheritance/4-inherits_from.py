#!/usr/bin/python3
"""Defines a function to check for inherited instance of a class.
"""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class;
    otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
