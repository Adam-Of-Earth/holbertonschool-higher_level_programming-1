#!/usr/bin/python3
"""Module to return the request id of the header"""
import sys
import urllib.request


with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.headers.get("X-Request-Id"))
