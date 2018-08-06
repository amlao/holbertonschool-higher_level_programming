#!/usr/bin/python3
"""
a Python script that takes your Github credentials (username and password)
and uses the Github API to display your id
"""
import requests
from requests.auth import HTTPBasicAuth
import sys
from sys import argv

if __name__ == "__main__":
    user = sys.argv[1]
    pw = sys.argv[2]
    que = requests.get("https://api.github.com/user",
                       auth=HTTPBasicAuth(user, pw))
    print(que.json().get("id"))
