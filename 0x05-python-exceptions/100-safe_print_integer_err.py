#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{}".format(value))
    except ValueError as err:
        sys.stderr.write("Exception: {}\n".format(err))
        return False
    finally:
        pass
    return True
