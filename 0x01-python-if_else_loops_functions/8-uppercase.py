#!/usr/bin/python3
def uppercase(str):
    result = ""
    for i in str:
        x = ord(i)
        if x > 96 and x < 123:
            x -= 32
        result += chr(x)
    print("{}".format(result))
