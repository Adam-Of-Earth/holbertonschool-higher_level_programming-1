#!/usr/bin/python3
"""Module to send post request to web resource"""
import sys
import requests


if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) < 2:
        payload = {"q": "''"}
    else:
        payload = {"q": sys.argv[1]}
    req = requests.post(url, payload)
    try:
        payload = req.json()
    except ValueError:
        print("Not a valid JSON")
    else:
        if hasattr(payload, "__contains__") and len(payload) < 1:
            print("No Result")
        else:
            print("[{}] {}".format(payload["id"], payload["name"]))
