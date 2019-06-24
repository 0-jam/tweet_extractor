import argparse
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description='Extract text from tweets collected by bulk_tweet_searcher.py')
    parser.add_argument('input', type=str, help='Input file path')
    parser.add_argument('--output', type=str, help="Output directory path (default: 'Same as input filename without extension')")
    args = parser.parse_args()

    inpath = Path(args.input)
    with inpath.open(encoding='utf-8') as input:
        trending_tweets = json.load(input)

    if args.output:
        outdir = Path(args.output)
    else:
        outdir = Path(inpath.stem)

    if not outdir.is_dir():
        Path.mkdir(outdir, parents=True)

    for count, (topic, tweets) in enumerate(trending_tweets.items(), start=1):
        with outdir.joinpath('tweets_{:03}.txt'.format(count)).open('w', encoding='utf-8') as tweets_out:
            tweets_out.writelines([tweet['text'] for tweet in tweets['tweets']])

        with outdir.joinpath('topics.txt').open('a', encoding='utf-8') as topics_out:
            topics_out.write(topic + '\n')


if __name__ == "__main__":
    main()
