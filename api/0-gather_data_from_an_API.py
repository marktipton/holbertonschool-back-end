#!/usr/bin/python3
"""
using a sample REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests

get_employee = requests.get("https://jsonplaceholder.typicode.com/users")
get_todos = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print(get_employee.status_code)
print(get_employee.json())

print(get_todos.status_code)
print(get_todos.json())

employee = get_employee.json()[0]['name']

comp_tasks = get_todos.json()['completed']

tot_tasks = get_todos.json()['title']

print(f'Employee {employee} is done with tasks({comp_tasks}/{tot_tasks})')
