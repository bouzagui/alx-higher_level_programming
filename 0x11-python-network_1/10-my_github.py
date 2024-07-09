#!/usr/bin/python3
""" module """
import requests
import sys

if __name__ == "__main__":
    user = sys.argv[1]
    password = sys.argv[2]
    url = "https://api.github.com/user"
    headers = {'Authorization': f'Bearer {password}'}
    res = requests.get(url, headers=headers)
    if (res.status_code >= 400):
        print("None")
        exit()
    print(res.json()["id"])