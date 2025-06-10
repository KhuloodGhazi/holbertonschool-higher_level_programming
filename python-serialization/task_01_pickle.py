#!/usr/bin/python3
"""Module to demonstrate custom object serialization with pickle."""

import pickle
import os


class CustomObject:
    """A simple class to represent a custom object."""

    def __init__(self, name, age, is_student):
        """Initialize attributes."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize the object to the given filename using pickle."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception:
            pass  # Ignore errors silently as per instruction

    @classmethod
    def deserialize(cls, filename):
        """Deserialize a CustomObject from the given filename."""
        if not os.path.exists(filename):
            return None
        try:
            with open(filename, 'rb') as f:
                obj = pickle.load(f)
                if isinstance(obj, cls):
                    return obj
                return None
        except Exception:
            return None
