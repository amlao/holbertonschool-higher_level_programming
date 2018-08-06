#!/usr/bin/python3
"""
a Python script that takes in a URL and an email, sends a POST requestto the
passed URL with the email as a parameter and displays the body of the response
"""
import urllib.request
import urllib.parse
import sys
from sys import argv


if __name__ == "__main__":
    body = sys.argv[1]
    info = {}
    info['email'] = sys.argv[2]
    data = urllib.parse.urlencode(info)
    data = data.encode('ascii')
    req = urllib.request.Request(body, data)
    with urllib.request.urlopen(req) as decode:
        print(decode.read().decode('utf-8'))
