# Tweet Extractor

- Test for Twitter API

---

1. [Todo](#todo)
1. [Installation](#installation)
1. [Usage](#usage)
   1. [tweet_searcher.py](#tweet_searcherpy)
   1. [trend_searcher.py](#trend_searcherpy)

---

## Todo

- [x] Search trends by a specified location
- [x] Search tweets by a specified word
- [x] Connect to API

## Installation

```bash
# Common
$ pip install tweepy python-dotenv --user

# trend_searcher.py
$ pip install googlemaps --user
```

## Usage

- `-h` to show help

### tweet_searcher.py

`$ python tweet_searcher.py 'Radeon RX 5700' --output rdna.json --count 50`

### trend_searcher.py

`$ python trend_searcher.py --query '東京' --output trends_tokyo.json`
