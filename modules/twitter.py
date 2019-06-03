# Initialize Twitter API and load some modules
import tweepy
import modules.gmaps as gmaps

import settings

assert settings.TWITTER_API_KEY
assert settings.TWITTER_API_SECRET
api = tweepy.API(tweepy.OAuthHandler(settings.TWITTER_API_KEY, settings.TWITTER_API_SECRET))


# Search tweets by query and returns them as single dict format
def search_tweet(query, count=100):
    tweets = api.search(q=query, count=count)
    return {tweet.id: tweet._json for tweet in tweets}


# 1 is the ID of global trends
def search_trends_by_id(place_id=1):
    return api.trends_place(place_id)


def search_trends_by_latlng(latlng):
    place = api.trends_closest(*latlng)[0]
    place_id = place['woeid']

    # The location of trends can be different from specified location
    print('Retrieving trends ID: {} ({}) ...'.format(place_id, place['name']))
    return search_trends_by_id(place_id)


def search_trends_by_query(query):
    locations = gmaps.geocode(query)

    if locations:
        latlng = locations[0]['geometry']['location'].values()
        trends = search_trends_by_latlng(latlng)
    else:
        print('No location found. Retrieving global trends ...')
        trends = search_trends_by_id()

    return trends
