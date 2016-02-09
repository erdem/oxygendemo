import json
import re
import urllib2
from urllib import urlencode
from decimal import Decimal

from oxygendemo.constants import EXCHANGE_RATE_API_URL


def clean_price(price_str):
    price = re.sub(r'[^0-9.]+', '', price_str)
    return Decimal(price)


def get_exchange_rates(currency="GBP"):
    api_params = urlencode({"base": currency})
    api_url = '{0}?{1}'.format(EXCHANGE_RATE_API_URL, api_params)

    try:
        response = urllib2.urlopen(api_url)
        return json.loads(response.read())['rates']
    except (KeyError, urllib2.HTTPError):
        raise Exception("Could not found exhange rates")


def find_best_match(info_words, key_map):
    """
    :param info <list>:
    :param key_map <dict>:
    """
    matches = []
    for key, values in key_map.items():
        match_count = sum([info_words.count(m) for m in values])
        d = {
            "name": key,
            "count": match_count
        }
        matches.append(d)

    matches = sorted(matches, key=lambda k: k['count'], reverse=True)
    return matches[0]
