#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        print(response.read())
