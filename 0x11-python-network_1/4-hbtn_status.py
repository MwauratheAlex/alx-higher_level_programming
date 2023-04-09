#!/usr/bin/python3
"""fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    import requests

    url = "https://alx-intranet.hbtn.io/status"
    print("Body response:")

    with requests.get(url) as response:
        r = response.text
        print("\t- type: {}".format(type(r)))
        print("\t- content: {}".format(r))
