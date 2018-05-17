#!/usr/bin/python3


from json import dumps


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding="UTF8") as file:
        file.write(dumps(my_obj))
