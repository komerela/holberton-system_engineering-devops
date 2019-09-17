#!/usr/bin/python3
"""
using this REST API, for a given ID, returns info about his/her TODO list
"""
import urllib
import requests
import sys

if __name__ == "__main__":

    url_todos = 'https://jsonplaceholder.typicode.com/todos/'
    url_users = 'https://jsonplaceholder.typicode.com/users/'
    todos_list = requests.get(url_todos, params={'userId': sys.argv[1]})

    users_list = requests.get(url_users, params={'id': sys.argv[1]})
    todo_lst = todos_list.json()
    usr_lst = users_list.json()
    com_tasks = []
    all_tasks = len(todo_lst)
    employee = usr_lst[0].get('name')

    for task in todo_lst:
        if task.get('completed') is True:
            com_tasks.append(task)

    print("Employee {} is done with tasks({}/{}):"
          .format(employee, len(com_tasks), all_tasks))

    for task in com_tasks:
        print("\t {}".format(task.get('title')))
