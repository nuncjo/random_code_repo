# -*- coding:utf-8 -*-

'''
DuckDuckGo simple scraper
'''

from urllib.parse import quote
import requests
from descriptors import Answer


def scrape(question):
    if not question:
        raise Exception("Please provide a question")

    url = "http://api.duckduckgo.com/?q={}&format=xml&pretty=1".format(quote(question))
    response = requests.get(url).content
    answer = Answer(response)
    heading = answer.related_topics
    print(heading)

scrape("Google")



