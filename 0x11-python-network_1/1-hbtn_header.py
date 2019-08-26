#!/usr/bin/python3
"""Module to return the request id of the header"""
import sys
import urllib.request as request


url = str(sys.argv[1])
with request.urlopen(url) as response:
    print(response.headers.get("X-Request-Id"))
