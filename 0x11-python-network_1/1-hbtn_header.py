#!/usr/bin/python3
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.__getitem__('X-Request-Id'))
