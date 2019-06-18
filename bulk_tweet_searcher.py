import argparse
import json
from pathlib import Path

import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search trends in a specified location and collect tweets from trends')
    # Optional arguments
    parser.add_argument('--location', type=str, help='Location name (default: None (collect global trends))')
    parser.add_argument('--output', type=str, default='trends.json', help='Output file path (default: trending_tweets.json)')
    args = parser.parse_args()

    if args.location:
        trends = twitter.search_trends_by_query(args.location)
    else:
        print('Location is not specified. Retrieving global trends ...')
        trends = twitter.search_trends_by_id()

    trend_names = [trend['name'] for trend in trends[0]['trends']]

    tweets = {trend: twitter.search_tweet(trend) for trend in trend_names}

    with Path(args.output).open('w', encoding='utf-8') as out_json:
        out_json.write(json.dumps(tweets, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
