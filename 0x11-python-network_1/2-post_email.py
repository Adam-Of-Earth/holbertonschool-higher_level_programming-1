#!/usr/bin/python3
"""Module to post data to a webpage"""
import sys
import urllib.request as request


if __name__ == "__main__":
    with request.urlopen(sys.argv[1],
                         b"email=" + sys.argv[2].encode()) as request:
                            print(request.read().decode("UTF-8"))
