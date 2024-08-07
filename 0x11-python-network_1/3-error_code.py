#!/usr/bin/python3
"""models"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as res:
            body = res.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
