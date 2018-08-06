#!/usr/bin/python3
"""
a Python script that takes in a string and sends a search request
to the Star Wars API
"""
import requests
from sys import argv


if __name__ == "__main__":
    req = requests.get('https://swapi.co/api/people',
                       params={'search': argv[1]})
    counter = req.json().get('count')
    res = req.json().get('results')
    print("Number of results:", counter)
    if counter:
        for singular in res:
            print(singular['name'])
        flw = counter.get('next')
        while flw is not None:
            rn = requests.get(flw)
            for ent in res:
                print(ent['name'])
