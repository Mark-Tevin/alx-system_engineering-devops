#!/usr/bin/python3
"""Exports to-do list info from a given employee ID to JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    url_api = "https://jsonplaceholder.typicode.com/"
    user = requests.get(f"{url_api}users/{user_id}").json()
    username = user.get("username")
    todos = requests.get(f"{url_api}todos", params={"userId": user_id}).json()

    with open(f"{user_id}.json", "w") as jsonfile:
        json.dump(
            {user_id: [
                {
                    "task": t.get("title"),
                    "completed": t.get("completed"),
                    "username": username
                } for t in todos
            ]},
            jsonfile,
            indent=4  # Optional: for readability in the JSON file
        )
