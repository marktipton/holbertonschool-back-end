#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
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

    # initialize variables
    employee_counts = {}
    comp_tasks = 0
    tot_tasks = 0
    # cannot iterate over response object directly so store in another variable
    todos_data = get_todos.json()
    employee_data = get_employee.json()

    # for employee in employee_data:
    #     user_id = employee["id"]

    # recorrect user index from argv
    user_id_index = user_id + 1
    employee_counts[user_id_index] = {"completed": 0, "total": 0}


    for todo in todos_data:
        if user_id_index == todo["userId"]:

            employee_counts[user_id_index]["total"] += 1

            if todo["completed"]:
                employee_counts[user_id_index]["completed"] += 1

    comp_tasks = employee_counts[user_id_index]["completed"]
    tot_tasks = employee_counts[user_id_index]["total"]
    # print first line
    print(
        f'Employee {employee_name} is done with tasks({comp_tasks}/{tot_tasks}):'
    )

    for todo in todos_data:
        if todo["completed"] and user_id_index == todo["userId"]:
            print(f'     {todo["title"]}')


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    gather_data()