#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
extend previous script to export data in the JSON format.
Records all tasks owned by an employee
"""
import json
import requests
import sys


def gather_data():
    """
    using a sample REST API, for a given employee ID,
    returns information about his/her TODO list progress.
    """
    # get json data from api
    get_employee = requests.get("https://jsonplaceholder.typicode.com/users")
    get_todos = requests.get("https://jsonplaceholder.typicode.com/todos")

    user_id = int(sys.argv[1]) - 1
    employee_name = get_employee.json()[user_id]['name']
    user_name = get_employee.json()[user_id]['username']

    # initialize variables
    employee_counts = {}
    comp_tasks = 0
    total = 0
    # cannot iterate over response object directly so store in another variable
    todos_data = get_todos.json()
    employee_data = get_employee.json()

    # for employee in employee_data:
    #     user_id = employee["id"]

    # recorrect user index from argv
    user_id_index = user_id + 1
    employee_counts[user_id_index] = {"completed": 0, "total": 0}

    tasks = []

    for todo in todos_data:
        if user_id_index == todo["userId"]:
            task_info = {
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_name
            }
            tasks.append(task_info)

    # comp_tasks = employee_counts[user_id_index]["completed"]
    # total = employee_counts[user_id_index]["total"]
    # # print first line
    # print(
    #     f'Employee {employee_name} is done with tasks({comp_tasks}/{total}):'
    # )

    # for todo in todos_data:
    #     if todo["completed"] and user_id_index == todo["userId"]:
    #         print(f'\t {todo["title"]}')

    json_data = {str(user_id_index): tasks}

    filename = f"{user_id_index}.json"

    with open(filename, 'w') as json_file:
        json.dump(json_data, json_file, indent=2)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    gather_data()
