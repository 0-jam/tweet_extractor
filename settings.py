import os

from dotenv import load_dotenv

load_dotenv()

TWITTER_API_KEY = os.environ.get('TWITTER_API_KEY')
TWITTER_API_SECRET = os.environ.get('TWITTER_API_SECRET')

GMAPS_API_KEY = os.environ.get('GOOGLE_API_KEY')
