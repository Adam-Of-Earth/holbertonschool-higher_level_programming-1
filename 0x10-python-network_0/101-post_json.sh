#!/bin/bash
# POST a json file
curl -Hs 'Content-Type: application/json' -d @"$2" "$1"
