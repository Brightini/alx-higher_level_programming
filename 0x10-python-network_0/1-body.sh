#!/bin/bash
# This script takes a URL, sends a GET request and display the body of a 200 status code response

URL=$1
response=$(curl -s -w "%{http_code}" "$URL")

# Extract the last 3 characters as the status code
status_code=${response: -3}
# Extract the response body, removing the status code
body=${response%"$status_code"}

if [[ $status_code == "200" ]]; then
	echo "$body"
else
	echo "Error: Unexpected status code $status_code"
fi
