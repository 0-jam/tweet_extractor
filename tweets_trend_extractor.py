import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Extract trends from tweets collected by tweet_searcher.py')
    parser.add_argument('input', type=str, help='Input file path')
    parser.add_argument('output', type=str, help='Output file path')
    args = parser.parse_args()

    with Path(args.input).open(encoding='utf-8') as input:
        trends = json.load(input)

    trend_names = [trend['name'] for trend in trends['trends']]

    with Path(args.output).open('w', encoding='utf-8') as out:
        out.write('\n'.join(trend_names))


if __name__ == "__main__":
    main()
