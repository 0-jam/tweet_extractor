import argparse
import json
from pathlib import Path

import modules.gmaps as gmaps
import modules.twitter as twitter


def main():
    parser = argparse.ArgumentParser(description='Search trends in a specified location')
    # Optional arguments
    parser.add_argument('--query', type=str, help='Location name (default: None (collect global trends))')
    parser.add_argument('--output', type=str, default='trends.json', help='Output file path (default: results.json)')
    args = parser.parse_args()

    locations = gmaps.geocode(args.query)

    if locations:
        latlng = locations[0]['geometry']['location'].values()
        trends = twitter.search_trends_by_latlng(latlng)
    else:
        print('Location is not specified. Retrieving global trends ...')
        trends = twitter.search_trends_by_id()

    with Path(args.output).open('w', encoding='utf-8') as out:
        out.write(json.dumps(trends, ensure_ascii=False, indent=4))


if __name__ == "__main__":
    main()
