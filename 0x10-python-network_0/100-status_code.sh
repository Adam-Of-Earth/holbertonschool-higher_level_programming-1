#!/bin/bash
# Display status code
curl -s -o /dev/null -w '%{http_code}' "$@"
