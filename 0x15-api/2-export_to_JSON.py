#!/usr/bin/python3
""" Extends task 1 to export data in the JSON format """
from requests import get
from sys import argv
import json


def to_json(employee_id):
    """ Uses get to pull data and exports data in a JSON format """
    users = get("https://jsonplaceholder.typicode.com/users/" +
                employee_id).json()
    todos = get("https://jsonplaceholder.typicode.com/todos?userId=" +
                employee_id).json()
    if not users or not todos:
        return ("Not a valid JSON")
    task_list = []
    for task in todos:
        task_dict = {}
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = users.get('username')
        task_list.append(task_dict)
    data = {}
    data[employee_id] = task_list
    with open('{}.json'.format(employee_id), 'w') as file:
        json.dump(data, file)


if __name__ == "__main__":
    if len(argv) > 1:
        to_json(argv[1])
