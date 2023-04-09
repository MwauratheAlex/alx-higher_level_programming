#!/usr/bin/python3
"""takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter."""


if __name__ == "__main__":
    import sys
    import requests

    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]

    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    with requests.post(url, data=data) as response:
        try:
            json = response.json()
            if len(json) == 0:
                print("No result")
            else:
                print("[{}] {}".format(json.get("id"), json.get("name")))
        except ValueError:
            print("Not a valid JSON")
