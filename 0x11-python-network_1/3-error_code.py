#!/usr/bin/python3
"""Module to display error code coming from a web resource"""
import sys
import urllib.request as request
from urllib.error import URLError, HTTPError


if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            html = response.read()
            print(html.decode("UTF-8"))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
