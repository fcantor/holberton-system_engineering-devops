#!/usr/bin/python3
""" Extends task 1 to export data in the CSV information """
from requests import get
from sys import argv
import csv


def get_data(employee_id):
    """ Uses get to pull data and exports data in a CSV format """
    users = get("https://jsonplaceholder.typicode.com/users/" +
                employee_id).json()
    todos = get("https://jsonplaceholder.typicode.com/todos?userId=" +
                employee_id).json()
    if not users or not todos:
        return ("Not a valid JSON")
    with open('{}.csv'.format(employee_id), 'w') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([employee_id,
                             users.get('name'),
                             task.get('completed'),
                             task.get('title')])


if __name__ == "__main__":
    if len(argv) > 1:
        get_data(argv[1])
