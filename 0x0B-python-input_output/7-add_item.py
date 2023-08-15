#!/usr/bin/python3
"""loads, adds and saves arguments to a Python list"""
from sys import argv


load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

try:
    json_list = load('add_item.json')
except (ValueError, FileNotFoundError):
    json_list = []

for item in argv[1:]:
    json_list.append(item)

save(json_list, 'add_item.json')
