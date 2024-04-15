#!/usr/bin/python3
"""Saves informations from a given user ID to a .csv file"""

import requests
import csv
from sys import argv

API_URL = "https://jsonplaceholder.typicode.com/"

if __name__ == "__main__":
    # Get user and tasks informations
    user = requests.get(f'{API_URL}/users/{argv[1]}').json()
    todo_list = requests.get(f"{API_URL}/todos?userId={argv[1]}").json()

    # Open a new .csv file
    with open(f"{argv[1]}.csv", mode="w") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write into the csv file
        for task in todo_list:
            csv_writer.writerow([
                user['id'],
                user['username'],
                task['completed'],
                task['title']
            ])
