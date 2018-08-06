#!/usr/bin/python3
"""
a Python script that fetches https://intranet.hbtn.io/status
"""
import urllib.request


with urllib.request.urlopen('https://intranet.hbtn.io/status') as decode:
    body = decode.read()
    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
    print("\t- utf8 content:", body.decode("utf-8"))
