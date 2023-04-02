#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and displays
the body of the response"""


if __name__ == "__main__":
    import sys
    import urllib.request
    from urllib.error import URLError

    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as response:
            print(response.read().decode('utf-8'))
    except URLError as e:
        print('Error code:', e.code)
