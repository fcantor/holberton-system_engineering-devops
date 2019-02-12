#!/usr/bin/python3
""" Extends task 1 to export data in the JSON format """
from requests import get
from sys import argv
import json


def all_to_json():
    """ Uses get to pull data and exports data in a CSV format """
    users = get("https://jsonplaceholder.typicode.com/users/").json()
    todos = get("https://jsonplaceholder.typicode.com/todos").json()
    if not users or not todos:
        return ("Not a valid JSON")
    user_dict = {}
    username_dict = {}
    for user in users:
        employee_id = user.get('id')
        user_dict[employee_id] = []
        username_dict[employee_id] = user.get('username')
    for task in todos:
        task_dict = {}
        employee_id = task.get('userId')
        task_dict['task'] = task.get('title')
        task_dict['completed'] = task.get('completed')
        task_dict['username'] = username_dict.get(employee_id)
        user_dict.get(employee_id).append(task_dict)
    with open('todo_all_employees.json', 'w') as file:
        json.dump(user_dict, file)


if __name__ == "__main__":
    all_to_json()
