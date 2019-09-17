#!/usr/bin/python3
"""
Pings a To-Do API for data for all users and writes it to a JSON file
"""

import csv
import json
import requests
import sys

if __name__ == '__main__':

    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    users = requests.get(url_users).json()
    employee_id = 1
    user_tasks = {}

    for employee_id in range(1, len(users) + 1):
        todos_list = requests.get(url_todos, params={'userId': employee_id})
        users_list = requests.get(url_users, params={'id': employee_id})
        todo_lst = todos_list.json()
        usr_lst = users_list.json()
        employee = usr_lst[0].get('username')
        task_list = []
        employee = usr_lst[0].get('username')

        for task in todo_lst:
            status = task.get('completed')
            title = task.get('title')
            task_dic = {}
            task_dic['task'] = title
            task_dic['completed'] = status
            task_dic['username'] = employee
            task_list.append(task_dic)
        user_tasks[employee_id] = task_list

    with open("todo_all_employees.json", "w+") as jsonfile:
        json.dump(user_tasks, jsonfile)
