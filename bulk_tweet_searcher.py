import argparse
import json
from datetime import datetime
from pathlib import Path

from tqdm import tqdm

import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search trends in a specified location and collect tweets from trends')
    # Optional arguments
    parser.add_argument('--locale', type=str, help='Location name (default: None (collect global trends))')
    args = parser.parse_args()

    if args.locale:
        trends = twitter.search_trends_by_query(args.locale)
    else:
        print('Location is not specified. Retrieving global trends ...')
        trends = twitter.search_trends_by_id()

    locale = trends['locations'][0]['name']
    today = datetime.today().strftime('%Y%m%d%H%M')

    # Save retrieved trends as the same format of trend_searcher.py
    print('Saving trends...')
    with Path('trends_{}_{}.json'.format(locale, today)).open('w', encoding='utf-8') as out:
        out.write(json.dumps(trends, ensure_ascii=False, indent=2))

    trend_names = [trend['name'] for trend in trends['trends']]
    tweets = {trend: twitter.search_tweet(trend) for trend in tqdm(trend_names, desc='Retrieving tweets...')}

    # Output tweets as the JSON file
    # format: {topic: [tweets], topic2: [tweets], ...}
    print('Saving tweets...')
    with Path('tweets_{}_{}.json'.format(locale, today)).open('w', encoding='utf-8') as out_json:
        out_json.write(json.dumps(tweets, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
