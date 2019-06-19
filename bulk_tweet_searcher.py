import argparse
import json
from pathlib import Path
from datetime import datetime

import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search trends in a specified location and collect tweets from trends')
    # Optional arguments
    parser.add_argument('--locale', type=str, help='Location name (default: None (collect global trends))')
    parser.add_argument('--output', type=str, default='trending_tweets_{}.json'.format(datetime.today().strftime('%Y%m%d%H%M')), help='Output file path (default: trending_tweets_<YYYYMMDDHHMM>.json)')
    args = parser.parse_args()

    if args.locale:
        trends = twitter.search_trends_by_query(args.locale)
    else:
        print('Location is not specified. Retrieving global trends ...')
        trends = twitter.search_trends_by_id()

    trend_names = [trend['name'] for trend in trends[0]['trends']]

    tweets = {trend: twitter.search_tweet(trend) for trend in trend_names}

    with Path(args.output).open('w', encoding='utf-8') as out_json:
        out_json.write(json.dumps(tweets, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
