import os

from dotenv import load_dotenv

load_dotenv()

TWITTER_ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_SECRET = os.environ.get('TWITTER_ACCESS_SECRET')

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET')

TWITTER_BEARER_TOKEN = os.environ.get('TWITTER_BEARER_TOKEN')