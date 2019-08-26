#!/usr/bin/python3
"""Module to get an ID of a GitHub user"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(
        "https://api.github.com/user",
        auth=(sys.argv[1], sys.argv[2])
    )
    print(req.json().get("if"))
