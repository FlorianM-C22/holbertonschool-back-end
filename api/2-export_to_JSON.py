#!/usr/bin/python3
"""Export data from a REST API to a JSON file"""
import json
import requests
from sys import argv, exit


if __name__ == "__main__":
    API_URL = "https://jsonplaceholder.typicode.com"
    EMPLOYEE_ID = argv[1]

    response = requests.get(
        f"{API_URL}/users/{EMPLOYEE_ID}/todos",
        params={"_expand": "user"}
    )
    data = response.json()

    if not len(data):
        print("RequestError:", 404)
        exit(1)

    user_tasks = {EMPLOYEE_ID: []}
    for task in data:
        task_dict = {
            "task": task["title"],
            "completed": task["completed"],
            "username": task["user"]["username"]
        }
        user_tasks[EMPLOYEE_ID].append(task_dict)

    with open(f"{EMPLOYEE_ID}.json", "w") as file:
        json.dump(user_tasks, file)
