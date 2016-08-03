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

# License
>(c) 2016 Vivek Singh Bhadauria 

>This is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 

>This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

>You should have received a copy of the GNU General Public License along with this app. If not, see <http://www.gnu.org/licenses/>. 

