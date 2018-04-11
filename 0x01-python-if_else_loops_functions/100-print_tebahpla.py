#!/usr/bin/python3
for i in reversed(range(122, 96, -1)):
    if i % 2 != 0:
        i -= 32
    print("{}".format(i), end="")
