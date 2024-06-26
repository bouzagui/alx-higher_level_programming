#!/usr/bin/python3
""" saves to json file """
import json


def save_to_json_file(my_obj, filename, ):
    """ Save the object to a file """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(json.dumps(my_obj))
