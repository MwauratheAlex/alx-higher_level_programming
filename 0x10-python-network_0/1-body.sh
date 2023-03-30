#!/bin/bash
#takes in a URL, sends a GET request to the URL, and displays the body of the response
response=$(curl -X GET -s -o /dev/null -w "%{http_code}" $1)

if [ $response -eq 200 ]; then
	curl $1
fi
