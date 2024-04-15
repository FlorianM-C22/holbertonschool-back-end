#!/usr/bin/python3
"""Returns information for a given employee ID using a REST API"""

import requests
from sys import argv

API_URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    # Tasks information
    todos = requests.get(f'{API_URL}/todos?userId={argv[1]}')
    todos_data = todos.json()

    # User information
    users = requests.get(f'{API_URL}/users/{argv[1]}')
    users_data = users.json()

    completed_tasks = [task for task in todos_data if task['completed']]

    user_name = users_data["name"]
    len_completed_tasks = len(completed_tasks)
    total_todo = len(todos_data)

    print("Employee {} is done with tasks({}/{}):".format(
            user_name,
            len_completed_tasks,
            total_todo))

    for task in completed_tasks:
        print(f"\t {task['title']}")
