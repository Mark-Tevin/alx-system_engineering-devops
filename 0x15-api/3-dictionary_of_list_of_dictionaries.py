#!/usr/bin/python3
"""Exports to-do list info of all employees to JSON format."""

import json
import requests

if __name__ == "__main__":
    url_api = "https://jsonplaceholder.typicode.com/"
    users = requests.get(f"{url_api}users").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                u.get("id"): [
                    {
                        "task": t.get("title"),
                        "completed": t.get("completed"),
                        "username": u.get("username")
                    }
                    for t in requests.get(
                        f"{url_api}todos", params={"userId": u.get("id")}
                    ).json()
                ]
                for u in users
            },
            jsonfile,
            indent=4  # Optional: for readability in the JSON file
        )
