import argparse
import json
from pathlib import Path

import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search tweets by query')
    # Required arguments
    parser.add_argument('query', type=str, help='Input file path')
    # Optional arguments
    parser.add_argument('--output', type=str, default='tweets.json', help='Output file path (default: tweets.json)')
    parser.add_argument('--count', type=int, default=100, help='The number of tweets to retrieve (default: 100)')
    args = parser.parse_args()

    tweets_dict = twitter.search_tweet(args.query, args.count)

    with Path(args.output).open('w', encoding='utf-8') as out_json:
        out_json.write(json.dumps(tweets_dict, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
