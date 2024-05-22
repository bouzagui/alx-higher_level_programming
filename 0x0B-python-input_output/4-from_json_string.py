#!/usr/bin/python3
""" implementation of the standard library functions """
import json


def from_json_string(my_str):
    """ Convert a JSON string into a list of objects """
    return json.loads(my_str)
