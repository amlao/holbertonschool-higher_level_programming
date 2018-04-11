#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) != 113 or chr(i) != 101:
    print("{:c}".format(i), end="")
