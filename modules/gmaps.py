import googlemaps

import settings

assert settings.GMAPS_API_KEY
api = googlemaps.Client(settings.GMAPS_API_KEY)


def geocode(query):
    if not query:
        print('No query specified. Skipping ...')
        return None

    try:
        print('Geocoding location:', query)
        return api.geocode(query)
    except Exception as e:
        print('Cannnot retrieve locations:', e)
        return None
