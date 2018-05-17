#!/usr/bin/python3


from sys import argv
save_to_json = __import__('7-save_to_json_file').save_to_json_file
load_from_json = __import__('8-load_from_json_file').load_from_json_file


try:
    test = load_from_json("add_item.json")
except:
    test = []
for args in argv[1:]:
    test.append(args)
save_to_json(test, "add_item.json")
