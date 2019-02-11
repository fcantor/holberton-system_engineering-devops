#!/usr/bin/python3
""" Python script that uses REST API to returns information about a given
employee's TODO list progress """
from requests import get
from sys import argv


def get_todos(employee_id):
    """ Uses get to pull todo tasks of passed in employee_id """
    users = get("https://jsonplaceholder.typicode.com/users/" +
                employee_id).json()
    todos = get("https://jsonplaceholder.typicode.com/todos?userId=" +
                employee_id).json()
    if not users or not todos:
        return ("Not a valid JSON")
    name = users.get('name')
    completed = [task.get('title') for task in todos if task.get('completed')]
    total_tasks_count = len(todos)
    completed_count = len(completed)
    print("Employee {} is done with tasks({}/{}):".format(name,
                                                          completed_count,
                                                          total_tasks_count))
    for t in completed:
        print("\t {}".format(t))


if __name__ == "__main__":
    if len(argv) > 1:
        get_todos(argv[1])
