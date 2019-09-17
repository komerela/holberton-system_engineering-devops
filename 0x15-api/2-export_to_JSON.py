#!/usr/bin/python3
"""
Pings a To-Do API for data for a specified user and writes it to a JSON file
"""
import csv
import json
import requests
import sys

if __name__ == '__main__':

    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    todos_list = requests.get(url_todos, params={'userId': sys.argv[1]})
    users_list = requests.get(url_users, params={'id': sys.argv[1]})

    todo_lst = todos_list.json()
    usr_lst = users_list.json()
    employee = usr_lst[0].get('username')

    task_list = []
    user_tasks = {}

    with open("{}.json".format(sys.argv[1]), "w+") as jsonfile:
        for task in todo_lst:
            status = task['completed']
            title = task['title']
            task = {}
            task['task'] = title
            task['completed'] = status
            task['username'] = employee
            task_list.append(task)
        user_tasks[sys.argv[1]] = task_list

        data = json.dumps(user_tasks)
        jsonfile.write(data)
