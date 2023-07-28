#!/bin/bash
# this script that takes in a URL, sends a request to that URL and gets a response (size in bytes)
response=$(curl -s -o /dev/null/ -w "%{size_download}" "$1"); echo $response
