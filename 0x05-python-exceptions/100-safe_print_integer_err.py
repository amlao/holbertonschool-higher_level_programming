#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{}".format(value))
    except ValueError:
        sys.stderr.write("Exception: {}\n".format(value))
        return False
    finally:
        pass
    return True
