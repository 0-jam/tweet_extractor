import argparse
import json
from datetime import datetime
from pathlib import Path

import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search trends in a specified location')
    # Optional arguments
    parser.add_argument('--locale', type=str, help='Location name (default: None (collect global trends))')
    parser.add_argument('--output', type=str, help='Output file path (default: trends_<locale>_<YYYYMMDDHHMM>.json)')
    args = parser.parse_args()

    if args.locale:
        trends = twitter.search_trends_by_query(args.locale)
    else:
        print('Location is not specified. Retrieving global trends ...')
        trends = twitter.search_trends_by_id()

    if args.output:
        outpath = Path(args.output)
    else:
        outpath = Path('trends_{}_{}.json'.format(trends['locations'][0]['name'], datetime.today().strftime('%Y%m%d%H%M')))

    with outpath.open('w', encoding='utf-8') as out:
        out.write(json.dumps(trends, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
