import re

from oxygendemo.constants import GPB_TO_USD_RATE, GPB_TO_EUR_RATE


def clean_price(price_str):
    price = re.sub(r'[^0-9.]+', '', unicode(price_str))
    return float(price)


def convert_gpb_to_usd(gpb_price):
    if not isinstance(gpb_price, float):
        gpb_price = clean_price(gpb_price)

    usd_price = gpb_price * GPB_TO_USD_RATE
    return "{0:.2f}".format(usd_price)


def convert_gpb_to_eur(gpb_price):
    if not isinstance(gpb_price, float):
        gpb_price = clean_price(gpb_price)

    eur_price = gpb_price * GPB_TO_USD_RATE
    return "{0:.2f}".format(eur_price)


def find_best_matches_key(info, key_map):
    """
    :param info <str>:
    :param key_map <dict>:
    """
    matches = []
    for key, values in key_map.items():
        match_count = sum([info.count(m) for m in values])
        d = {
            "name": key,
            "count": match_count
        }
        matches.append(d)

    matches = sorted(matches, key=lambda k: k['count'], reverse=True)
    return matches[0]

