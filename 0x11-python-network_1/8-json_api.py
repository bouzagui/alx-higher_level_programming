#!/usr/bin/python3
"""models """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    param = {"q": q}
    response = requests.post(url, data=param)
    try:
        json_data = response.json()
        if json_data:
            print(f"[{json_data['id']}] {json_data['name']}")
        else:
            print("No result")

    except Exception:
        print("Not a valid JSON")



#!/usr/bin/python3
""" module doc """
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    url = "http://0.0.0.0:5000/search_user"
    params = {"q": q}
    res = requests.post(url, data=params)
    try:
        resjson = res.json()
        if resjson:
            print(f'[{resjson["id"]}] {resjson["name"]}')
        else:
            print("No result")
    except Exception:
        print("Not a valid JSON")