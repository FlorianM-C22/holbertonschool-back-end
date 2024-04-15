#!/usr/bin/python3
"""Export data from a REST API to a JSON file"""
import json
import requests
from sys import argv, exit

API_URL = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    user_id = argv[1]

    response = requests.get(
        f"{API_URL}/users/{user_id}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        exit(1)

    user_tasks = {user_id: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks[user_id].append(task_dict)

    with open(f"{user_id}.json", "w") as file:
        json.dump(user_tasks, file)
