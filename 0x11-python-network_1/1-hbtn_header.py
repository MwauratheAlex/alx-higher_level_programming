#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays the value
of the X-Request-Id variable found in the header of the response."""
import sys
import urllib.request

with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
    print(response.headers.__getitem__('X-Request-Id'))
