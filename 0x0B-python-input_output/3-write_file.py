#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, encode="UTF8") as fo:
        return fo.write(text)
