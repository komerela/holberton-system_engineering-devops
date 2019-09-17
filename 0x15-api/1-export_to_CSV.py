#!/usr/bin/python3
"""
Pings a To-Do API for data on a specified user and saves the data to a CSV file
"""
import csv
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

    with open("{}.csv".format(sys.argv[1]), "a+") as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo_lst:
            status = task['completed']
            title = task['title']
            csvwriter.writerow(["{}".format(sys.argv[1]),
                                "{}".format(employee),
                                "{}".format(status),
                                "{}".format(title)])
