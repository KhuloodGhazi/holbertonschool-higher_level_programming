#!/usr/bin/env python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary to XML and save it to a file."""
    root = ET.Element('data')  # Create root element

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)  # Always store as string in XML

    tree = ET.ElementTree(root)
    try:
        tree.write(filename, encoding='utf-8', xml_declaration=True)
        return True
    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML from a file and return a dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        result = {}

        for child in root:
            result[child.tag] = child.text  # Read tag and its value as string

        return result
    except Exception:
        return None
