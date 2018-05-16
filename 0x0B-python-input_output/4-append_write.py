#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, encoding="UTF8") as fo:
        return fo.write(text)
