#!/usr/bin/python3
"""model"""
import requests


if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    get_con = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(get_con.text)))
    print("\t- content: {}".format(get_con.text))
