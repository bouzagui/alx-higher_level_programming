#!/bin/bash
# Send a POST request to the URL
url="$1"
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$url"
