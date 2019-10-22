from bs4 import BeautifulSoup
import requests
import random

popular_choice = ['motivational', 'life', 'positive', 'friendship', 'success', 'happiness', 'love']


def get_quotes(type, number_of_quotes=1):
    if " " not in type:
        url = "http://www.brainyquote.com/quotes/topics/topic_" + type + ".html"
    else:
        type.replace(" ","+")
        url = "https://www.brainyquote.com/search_results?q=" + type + ".html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    quotes = []
    authors = []
    for quote in soup.find_all('a', {'title': 'view quote'}):
        quotes.append("'" + quote.contents[0] + "'")
    for author in soup.find_all('a', {'title': 'view author'}):
        authors.append(" " + author.contents[0])
    #random.shuffle(quotes)
    final = list(map(str.__add__,quotes,authors))
    result = final[:number_of_quotes]
    return result

def get_random_quote():
    result = get_quotes(popular_choice[random.randint(0, len(popular_choice) - 1)])
    return result

