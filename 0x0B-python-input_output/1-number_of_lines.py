#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="UTF8") as file:
        line_num = 0
        for line in file:
            line_num += 1
    return line_num
