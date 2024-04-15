#!/usr/bin/python3
"""Returns information for a given employee ID using a REST API"""

import requests
from sys import argv
import csv

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    # Retrieve user data
    user_id = argv[1]
    user_response = requests.get(f'{API_URL}/users/{user_id}')
    user = user_response.json()

    # Retrieve todo list
    todo_response = requests.get(f"{API_URL}/todos?userId={user_id}")
    todo_list = todo_response.json()

    # Create CSV file
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                            "TASK_TITLE"])

        # Write data rows
        for todo in todo_list:
            csv_writer.writerow([user_id, user["username"], todo["completed"],
                                todo["title"]])
