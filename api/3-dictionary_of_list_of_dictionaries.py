#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
extends previous script to export data in the JSON format.
but now for all employees instead of one
"""
import json
import requests


def gather_data():
    """
    using a sample REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    # get json data from api
    get_employee = requests.get("https://jsonplaceholder.typicode.com/users")
    get_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    user_name = get_employee.json()[0]['username']

    # initialize variables
    employee_counts = {}

    # cannot iterate over response object directly so store in another variable
    todos_data = get_todos.json()
    employee_data = get_employee.json()

    all_employees_tasks = {}

    for employee in employee_data:
        tasks = []
        user_id = employee["id"]

        for todo in todos_data:
            task_info = {
                "username": employee["username"],
                "task": todo["title"],
                "completed": todo["completed"]
            }
            tasks.append(task_info)

        all_employees_tasks[str(user_id)] = tasks

    filename = f"todo_all_employees.json"

    with open(filename, 'w') as json_file:
        json.dump(all_employees_tasks, json_file, indent=2)


if __name__ == "__main__":
    gather_data()
