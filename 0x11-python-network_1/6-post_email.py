#!/usr/bin/python3
"""
a Python script that takes in a URL and an email address, sends a POST
request to the passed URL with the email as a parameter, and finally displays
the body of the response
"""
import requests
import sys
from sys import argv


if __name__ == "__main__":
    res = {'email': sys.argv[2]}
    req = requests.post(argv[1], data=res)
    print(req.text)
