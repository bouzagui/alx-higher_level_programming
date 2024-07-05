#!/usr/bin/python3
""" module """
import urllib.request

url = "https://alx-intranet.hbtn.io/status"
if __name__ == "__main__":
    with urllib.request.urlopen(url) as res:
        url_type = type(res)
        url_content = res.read()
        url_utf8 = url_content.decode("utf-8")
        print(f"Body response:\n\t- type: {url_type}\n\t\
                - content: {url_content}\n\t- utf8 content: {url_utf8}")
