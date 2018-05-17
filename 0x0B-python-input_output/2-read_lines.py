#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, encoding="UTF8") as file:
        if nb_lines <= 0:
            print(file.read(), end="")
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
