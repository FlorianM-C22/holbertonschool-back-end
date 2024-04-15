#!/usr/bin/python3
"""Script that saves infos from a given employee into a .csv file"""

import json
import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    user_id = argv[1]
    response = requests.get(f"{API_URL}/users/{user_id}/todos",
                            params={"_expand": "user"})
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

    # Write data to a JSON file
    with open(f"{user_id}.json", mode='w') as json_file:
        json.dump(data, json_file, indent=4)
