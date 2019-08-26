#!/usr/bin/python3
"""Module to post an email to a web resource"""
import sys
import requests


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    req = requests.post(url, {"email": email})
    print(req.text)
