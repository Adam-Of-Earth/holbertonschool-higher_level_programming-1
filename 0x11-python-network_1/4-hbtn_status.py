#!/usr/bin/python3
"""Gets info from a webpage using Requests"""
import requests


url = "https://intranet.hbtn.io/status"
req = requests.get(url)
print("Body response:")
print("\t- type: {}".format(type(req.text)))
print("\t- content: {}".format(req.text))
