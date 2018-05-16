#!/usr/bin/python3


from json import load


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF8") as file:
        load(file)
