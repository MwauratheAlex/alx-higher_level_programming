#!/usr/bin/python3
"""takes your GitHub credentials (username and password)
and uses the GitHub API to display your id"""


if __name__ == "__main__":
    import sys
    import requests
    from requests.auth import HTTPBasicAuth

    username = sys.argv[1]
    password = sys.argv[2]

    url = "https://api.github.com/user"
    auth = HTTPBasicAuth(username, password)

    with requests.get(url, auth=auth) as response:
        print(response.json().get("id"))
