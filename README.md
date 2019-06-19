# Tweet Extractor

- Test for Twitter API

---

1. [Todo](#Todo)
1. [Installation](#Installation)
1. [Prepare APIs](#Prepare-APIs)
   1. [Twitter API](#Twitter-API)
   1. [Google Maps API](#Google-Maps-API)
1. [Usage](#Usage)
   1. [tweet_searcher.py](#tweet_searcherpy)
   1. [trend_searcher.py](#trend_searcherpy)
   1. [tweets_text_extractor.py](#tweets_text_extractorpy)
   1. [tweets_trend_extractor.py](#tweets_trend_extractorpy)
   1. [bulk_tweet_searcher.py](#bulk_tweet_searcherpy)
   1. [bulk_tweet_extractor.py](#bulk_tweet_extractorpy)

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

`$ python tweet_searcher.py 'Radeon RX 5700' --output tweets_rdna.json --count 50`

### trend_searcher.py

`$ python trend_searcher.py --query '東京' --output trends_tokyo.json`

### tweets_text_extractor.py

`$ python tweets_text_extractor.py tweets_rdna.json tweets_rdna.txt`

### tweets_trend_extractor.py

`$ python tweets_trend_extractor.py trends_tokyo.json trends_tokyo.txt`

### bulk_tweet_searcher.py

- ATTENTION: This script emits a large JSON file
    - Open it as a text file may cause some problems due to large memory usage

`$ python bulk_tweet_searcher.py --location "東京" --output trending_tweets.json`

### bulk_tweet_extractor.py

`$ python bulk_tweet_extractor.py trending_tweets.json`
