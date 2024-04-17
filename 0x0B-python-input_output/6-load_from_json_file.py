#!/usr/bin/python3
""" load the specified directory and return it """
import json


def load_from_json_file(filename):
    """ load a json file """
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
