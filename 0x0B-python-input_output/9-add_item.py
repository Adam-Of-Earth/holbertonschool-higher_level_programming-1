#!/usr/bin/python3
"""Module to add arguments to a list, and save to file"""


import sys
import os.path


save_to_json_file = __import__("7-save_to_json_file").save_to_json_file
load_from_json_file = __import__("8-load_from_json_file").load_from_json_file

if os.path.isfile("add_item.json"):
    jstr = load_from_json_file("add_item.json")
    lst = sys.argv[1:len(sys.argv)]
    fstr = jstr + lst
    save_to_json_file(fstr, "add_item.json")
else:
    lst = sys.argv[1:len(sys.argv)]
    save_to_json_file(lst, "add_item.json")
