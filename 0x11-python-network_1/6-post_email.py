#!/usr/bin/python3
"""models"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email" : email}
    response = requests.get(url, data)
    print(response)