#!/bin/bash
# Requests with an extra header
curl -s -H 'X-HolbertonSchool-User-Id: 98' "$@"
