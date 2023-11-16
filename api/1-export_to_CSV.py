#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
extend previous script to export data in the CSV format.
"""
import csv
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
    csv_filename = f"{user_id_index}.csv"
    # employee_counts[user_id_index] = {"completed": 0, "total": 0}

    # for todo in todos_data:
    #     if user_id_index == todo["userId"]:

    #         employee_counts[user_id_index]["total"] += 1

    #         if todo["completed"]:
    #             employee_counts[user_id_index]["completed"] += 1

    # comp_tasks = employee_counts[user_id_index]["completed"]
    # total = employee_counts[user_id_index]["total"]
    # # print first line
    # print(
    #     f'Employee {employee_name} is done with tasks({comp_tasks}/{total}):'
    # )

    # for todo in todos_data:
    #     if todo["completed"] and user_id_index == todo["userId"]:
    #         print(f'\t {todo["title"]}')
    with open(csv_filename, mode='w', newline='') as csv_file:
        # fieldnames = []
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        for todo in todos_data:
            if user_id_index == todo["userId"]:
                writer.writerow([
                    str(user_id_index),
                    str(user_name),
                    str(todo["completed"]),
                    str(todo["title"])
                ])


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    gather_data()
