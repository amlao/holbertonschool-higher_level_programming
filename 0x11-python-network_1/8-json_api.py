#!/usr/bin/python3
"""
a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter
"""
import requests
import sys
from sys import argv


if __name__ == '__main__':
    if len(sys.argv) == 2:
        q = sys.argv[1]
    else:
        q = ""
    payload = {'q': q}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        id = response.json().get('id')
        name = response.json().get('name')
        if len(response.json()) == 0 or not id or not name:
            print("No result")
        else:
            print("[{}] {}".format(id, name))
    except BaseException:
        print("Not a valid JSON")
