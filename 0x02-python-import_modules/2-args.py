#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) - 1 < 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) - 1 == 1:
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
    for c in range(1, len(sys.argv)):
        print("{}: {}".format(c, sys.argv[c]))
