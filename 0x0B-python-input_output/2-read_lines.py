#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as file:
        for line in file:
            if nb_lines <= 0:
                break
            print(f.readline(), end="")
