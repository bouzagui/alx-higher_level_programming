#!/usr/bin/python3
""" module """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.request.urlopen(url) as res:
        url_type = type(res)
        url_content = res.read()
        url_utf8 = url_content.decode("utf-8")
        print("Body response:")
        print("\t- type: {}".format(url_type))
        print("\t- content: {}".format(url_content))
        print("\t- utf8 content: {}".format(url_utf8))
