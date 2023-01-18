#!/usr/bin/python3
"""
This module contains the function ``load_from_json_file(filename)``
The function creates an Object from a "JSON file"
"""

import json


def load_from_json_file(filename):
    """creates an Object from a "JSON file" """
    file = None
    with open(filename, 'r', encoding='utf-8') as f:
        file = json.loads(f.read())

    return file
