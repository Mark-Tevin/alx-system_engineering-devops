#!/usr/bin/python3
"""Returns a to-do list information for a given employee ID"""

import requests
import sys

if __name__ == "__main__":
    api_url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{api_url}users/{sys.argv[1]}").json()
    todos = requests.get(
        f"{api_url}todos", params={"userId": sys.argv[1]}
    ).json()

    completed = [t.get("title") for t in todos if t.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))
    for c in completed:
        print("\t {}".format(c))
