#!/usr/bin/python3
"""Module that uses Star Wars API to search for names"""
import sys
import requests


if __name__ == "__main__":
    req = requests.get(
        "https://swapi.co/api/people/",
        params={"search": sys.argv[1]}
    )
    req = req.json()
    print("Number of results:", req.get("count"))
    for person in req.get("results"):
        print(person.get("name"))
