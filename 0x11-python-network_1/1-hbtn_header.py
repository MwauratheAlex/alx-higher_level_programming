#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""
import urllib.request
import sys

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    print(response.headers.__getitem__('X-Request-Id'))
