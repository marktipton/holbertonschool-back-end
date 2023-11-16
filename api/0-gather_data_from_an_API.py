#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import sys
import requests


"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
get_employee = requests.get("https://jsonplaceholder.typicode.com/users")
get_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(get_employee.status_code)
# print(get_employee.json())

# print(get_todos.status_code)
# print(get_todos.json())
user_id = int(sys.argv[1]) - 1
employee_name = get_employee.json()[user_id]['name']

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

print(
    f'Employee {employee_name} is done with tasks({comp_tasks}/{tot_tasks}):'
)

for todo in todos_data:
    if todo["completed"] and user_id_index == todo["userId"]:
        print(f'     {todo["title"]}')
