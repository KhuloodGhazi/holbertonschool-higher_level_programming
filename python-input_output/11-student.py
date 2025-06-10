#!/usr/bin/python3
"""Class that defines a student"""


class Student:
    """Class that defines student with method"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if (
            isinstance(attrs, list)
            and all(isinstance(attr, str) for attr in attrs)
        ):
            return {
                key: getattr(self, key)
                for key in attrs
                if hasattr(self, key)
            }
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)
