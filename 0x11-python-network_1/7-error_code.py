#!/usr/bin/python3
"""takes in a URL, sends a request to the URL and
displays the body of the response."""


if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]

    with requests.get(url) as response:
        status_code = response.status_code

        if status_code >= 400:
            print("Error code: {}".format(status_code))
        else:
            print(response.text)
