#!/usr/bin/python3
'''
This module provides a function that writes JSON to a file.
'''
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    '''
    Serialize a Python dictionary to an XML file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): The name of the output XML file.
    '''
    root = ET.Element('data')

    for key, value in dictionary.items():
        element = ET.SubElement(root, key)
        element.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)


def deserialize_from_xml(filename):
    '''
    Deserialize an XML file back into a Python dictionary.

    Args:
        filename (str): The name of the input XML file.

    Returns:
        dict: The deserialized dictionary.
    '''
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        deserialized_dict = {child.tag: child.text for child in root}

        return deserialized_dict
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
        return None
