# pybrainyquote

Python Package to get quotes from [`BrainyQuote`](http://www.brainyquote.com/)

Install using pip:

    pip install brainyquote
    
## Dependencies :

     beautifulsoup4
     requests

## Install Dependencies :

    pip install beautifulsoup4
    pip install requests

## Usage

```python

from brainyquote import pybrainyquote

print(pybrainyquote.get_quotes('inspirational'))
print(pybrainyquote.get_quotes('motivational', 3))  # returns list with 3 quotes
print(pybrainyquote.get_random_quote())  # returns random quotes on popular_choice

```
All parameters are supported which are suggested in [`Topics`](http://www.brainyquote.com/quotes/topics.html)

Change **[popular_choice](https://github.com/viveksb007/pybrainyquote/blob/master/brainyquote/pybrainyquote.py)** for more random quotes

## Features
* returns number of quotes in list specified as ``` get_quotes( 'topic', number_of_quotes ) ```
* return any random quote from popular topics
