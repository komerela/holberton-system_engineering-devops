#!/usr/bin/python3
"""
Py script that returns total number of subreddit users
"""
import os
import requests

# def number_of_subscribers(subreddit):
#   page = requests.get('https://redditmetrics.com/r/')
#    htmlContent = html.fromstring(page.content)

#    body = htmlContent[1]
#    body = etree.tostring(body)
#     comment: Decode bitecode into a string
#    body = body.decode('UTF-8')
#    body = body.split('\n')
#    <td class="tod"' is where the info about the subs is.
#    body = [line for line in body if '<td class="tod"' in line] 
#    2D list, 3 attributes in inner lists - Rank, Subreddit URL and sub count
#    subredditInfo = []
#    for i in range(0, len(body), 3):
#        subredditInfo.append(body[i:i+3])

#    formatSubreddit = []
#    for subreddit in subredditInfo:
#        formatAttribute = []
#        for j, attribute in enumerate(subreddit):
#            if j == 0:
#                rank = attribute.split('>')[-2]
#                rank = rank.split('<')[0]
#                formatAttribute.append(rank)
#            if j == 1:
#                try:
#                    sub = attribute.split('</a></td>')[-2]
#                    sub = sub.split('>')[-1]
#                    formatAttribute.append('\thttps://www.reddit.com' + sub)
#                except IndexError:
#                    print(attribute)
#            if j == 2:
#                subscribers = attribute.split('</td>')[-2]
#                subscribers = subscribers.split('>')[-1]
#                formatAttribute.append('\t' + subscribers)
#
#        formatSubreddit.append(''.join(formatAttribute))

#    return formatSubreddit


def number_of_subscribers(subreddit):

    """Py script that returns total number of subreddit users"""

    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    user_agent = {'User-Agent': 'Koome@holberton'}
    req = requests.get(url, headers=user_agent, allow_redirects=False)
    if req.status_code == 200:
        req = req.json()
        data = req.get('data')
        subscribers = data.get('subscribers')
        if data is not None and subscribers is not None:
            return subscribers
    return 0
