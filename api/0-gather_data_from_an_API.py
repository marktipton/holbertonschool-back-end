#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests

get_employee = requests.get("https://jsonplaceholder.typicode.com/users")
get_todos = requests.get("https://jsonplaceholder.typicode.com/todos")
# print(get_employee.status_code)
# print(get_employee.json())

# print(get_todos.status_code)
# print(get_todos.json())

employee_name = get_employee.json()[0]['name']

employee_counts = {}
comp_tasks = 0

tot_tasks = 0
# cannot iterate over response object directly so store in another variable
todos_data = get_todos.json()
employee_data = get_employee.json()

for employee in employee_data:
    user_id = employee["id"]
    employee_counts[user_id] = {"completed": 0, "total": 0}

for todo in todos_data:
    user_id = todo["userId"]

    employee_counts[user_id]["total"] += 1

    if todo["completed"]:
        employee_counts[user_id]["completed"] += 1

comp_tasks = employee_counts[user_id]["completed"]
tot_tasks = employee_counts[user_id]["total"]

print(f'Employee {employee_name} is done with tasks({comp_tasks}/{tot_tasks})')
