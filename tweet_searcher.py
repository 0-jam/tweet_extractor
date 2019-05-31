import argparse
import json
from pathlib import Path

import tweepy

import settings

assert settings.TWITTER_API_KEY
assert settings.TWITTER_API_SECRET
twitter_api = tweepy.API(tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET))


def main():
    parser = argparse.ArgumentParser(description='Search tweets by query')
    # Required arguments
    parser.add_argument('query', type=str, help='Input file path')
    # Optional arguments
    parser.add_argument('--output', type=str, default='results.json', help='Output file path (default: results.json)')
    parser.add_argument('--count', type=int, default=100, help='The number of tweets to retrieve')
    args = parser.parse_args()

    tweets = twitter_api.search(q=args.query, count=args.count)
    tweets_dict = {tweet.id: tweet._json for tweet in tweets}

    with Path(args.output).open('w', encoding='utf-8') as out_json:
        out_json.write(json.dumps(tweets_dict, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    main()
