#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, 'w', encoding="UTF8") as fo:
        return fo.write(text)
