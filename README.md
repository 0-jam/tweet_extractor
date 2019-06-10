# Tweet Extractor

- Test for Twitter API

---

1. [Todo](#todo)
1. [Installation](#installation)
1. [Prepare APIs](#prepare-apis)
   1. [Twitter API](#twitter-api)
   1. [Google Maps API](#google-maps-api)
1. [Usage](#usage)
   1. [tweet_searcher.py](#tweet_searcherpy)
   1. [trend_searcher.py](#trend_searcherpy)

---

## Todo

- [ ] Remove retweeted (starts with 'RT')
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

## Prepare APIs

- Create `.env` file and add following lines

### Twitter API

- After creating Twitter Developer accounts and setting up development environment,

```bash
# Apps -> Details -> Keys and tokens -> Consumer API keys
# (API key)
TWITTER_API_KEY='key string here'
# (API secret key)
TWITTER_API_SECRET='key string here'
```

### Google Maps API

- After creating GCP project and acquiring 'Maps JavaScript API',

```bash
# Your GCP project's APIs & Services dashboard -> Maps JavaScript API -> Credentials -> "Key" column
GOOGLE_API_KEY='key string here'
```

## Usage

- `-h` to show help

### tweet_searcher.py

`$ python tweet_searcher.py 'Radeon RX 5700' --output rdna.json --count 50`

### trend_searcher.py

`$ python trend_searcher.py --query '東京' --output trends_tokyo.json`
