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

### Get quotes from topic

```python

from brainyquote import pybrainyquote

print(pybrainyquote.get_quotes('inspirational')) # returns one quote from the 'inspirational' topic
print(pybrainyquote.get_quotes('motivational', 3))  # returns list with 3 quotes from the 'motivational' topic
```

All parameters suggested in [`Topics`](http://www.brainyquote.com/quotes/topics.html) are supported.

### Get a single quote
```python
from brainyquote import pybrainyquote

print(pybrainyquote.get_random_quote())  # returns random quotes on popular_choice
```


Change **[popular_choice](https://github.com/viveksb007/pybrainyquote/blob/master/brainyquote/pybrainyquote.py)** for more random quotes

## Quote

All quotes returned follow the same format. First they contain the quote itself in single quotes, which is followed by the author.

### Example
```python
from brainyquote import pybrainyquote

quote = pybrainyquote.get_random_quote() 
# may return: "'Choosing to be positive and having a grateful attitude is going to determine how you're going to live your life.' Joel Osteen"
```


## Features
* returns number of quotes in list specified as ``` get_quotes( 'topic', number_of_quotes ) ```
* return any random quote from popular topics as ``` get_random_quote() ```

# License
>(c) 2016 Vivek Singh Bhadauria 

>This is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. 

>This software is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details. 

>You should have received a copy of the GNU General Public License along with this app. If not, see <http://www.gnu.org/licenses/>. 

