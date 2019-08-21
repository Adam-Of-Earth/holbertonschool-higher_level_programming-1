#!/bin/bash
# Displays all HTTP methods the server will accept
curl -si -X OPTIONS "$@" | grep "Allow" | cut -d ' ' -f 2
