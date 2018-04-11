#!/usr/bin/python3
for i in reversed(range(96, 123, +1)):
    if i % 2 != 0:
        i -= 32
    print("{:c}".format(i), end="")
