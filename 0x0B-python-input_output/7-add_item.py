#!/usr/bin/python3

'''
Load, add, save
'''


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    i = load_from_json_file("add_item.json")
except Exception:
    i = []
for x in range(1, len(sys.argv)):
    i.append(sys.argv[x])
save_to_json_file(i, "add_item.json")
