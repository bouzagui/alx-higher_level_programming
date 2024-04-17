#!/usr/bin/python3
""" convert a string to a list of strings """
import json
import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

list = []

try:
    filename = "add_item.json"
    list = load_from_json_file(filename)
except FileNotFoundError:
    pass
finally:
    for i in sys.argv:
        if i == sys.argv[0]:
            continue
        list.append(i)
    save_to_json_file(list, filename)
