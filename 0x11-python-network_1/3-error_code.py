#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL
and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys
from sys import argv


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as decode:
            print(decode.read().decode('utf-8'))

    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
