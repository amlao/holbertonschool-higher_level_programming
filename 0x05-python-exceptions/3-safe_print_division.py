#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        value = a / b
    except (TypeError, ZeroDivisionError):
        value = None
    finally:
        print("Inside result: {}".format(value))
    return value
