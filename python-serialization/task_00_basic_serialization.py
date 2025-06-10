#!/usr/bin/python3
"""Basic serialization module: save a dict to JSON and load it back."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): Dictionary to serialize.
        filename (str): File to save the JSON data into.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Deserialize JSON data from a file back into a dictionary.

    Args:
        filename (str): File to load JSON data from.

    Returns:
        dict: Deserialized dictionary.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
