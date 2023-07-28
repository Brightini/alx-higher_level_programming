#!/bin/bash
# This script takes a URL, sends a GET request and display the body of a 200 status code response
curl -s -w "\nResponse body:\n%{http_code}\n" "$1" | awk '/^Response body:$/{p=1;next}p'
