#!/bin/bash
# Find size of web resource in bytes
curl -Is "$@" | grep "Content-Length" | cut -d ' ' -f 2
