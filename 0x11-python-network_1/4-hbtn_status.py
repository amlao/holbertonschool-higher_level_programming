#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    req = requests.get('https://intranet.hbtn.io/status')
    rt = req.text
    print("Body response:")
    print("\t- type: {}".format(type(rt)))
    print("\t- content: {}".format(rt))
